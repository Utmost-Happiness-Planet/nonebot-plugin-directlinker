import time
from urllib.parse import urlencode

from nonebot import logger, on_shell_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, Message
from nonebot.rule import ArgumentParser
from nonebot.typing import T_State

from . import config

linker_group = config.linker_group
linker_command = config.linker_command

linker_parser = ArgumentParser(add_help=False)
linker_parser.add_argument("-h", "--help", dest="help", action="store_true")
linker_parser.add_argument("-n", "--name", dest="name")
linker_parser.add_argument("-i", "--info", dest="info", type=int)
linker_parser.add_argument("-p", "--path", dest="path")

linker = on_shell_command(linker_command, parser=linker_parser, priority=1)

help_text = f"""Manual of 群文件直链提取器
-n | --name     文件名.*
-i | --info     文件序号 
-p | --path     文件路径
例：/{linker_command} -n 文件名.exe
"""


@linker.handle()
async def link(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = str(event.group_id)
    if gid in linker_group or "all" in linker_group:
        args = vars(state.get("_args"))

        help = args.get('help')
        name = args.get('name')
        info = args.get('info')
        path = args.get('path')

        logger.debug(args)
        if help:
            await linker.finish(help_text)
        else:
            if not name and not path:
                await linker.finish(f"[Linker]语法错误，输入`/{linker_command} -h`查看帮助")

            await bot.send(event, "[Linker]处理中，请稍后…")
            root = await bot.get_group_root_files(group_id=int(event.group_id))
            files = {'root': root.get('files')}
            if root.get('folders'):
                for folder in root.get('folders'):
                    file = await bot.get_group_files_by_folder(group_id=int(event.group_id),
                                                               folder_id=folder['folder_id'])
                    files[folder['folder_name']] = file.get('files')
            # QQ群文件内不能套文件夹

            # # 广度优先搜索
            # d = deque()
            # if folders:
            #     d.extend([i["folder_id"] for i in folders])
            # while d:
            #     _ = d.popleft()
            #     logger.debug("下一个搜索的文件夹：" + _)
            #     root = await bot.get_group_files_by_folder(group_id=int(event.group_id), folder_id=_)
            #     folders = root.get("folders")
            #     file = root.get("files")
            #     if file:
            #         for i in file:
            #             files[i["file_name"]] = i
            #     if folders:
            #         d.extend([i["folder_id"] for i in folders])
            # logger.debug("共扫描出 " + str(len(files)) + " 个文件")

            # 搜索files 中文件 创建list

            if path:
                path = 'root' if path == '/' else path
                if files.get(path):
                    files = files[path]
                else:
                    await linker.finish("[Linker]并没有找到文件呢~是否文件路径输错了？")
            else:
                files = [i for i in files.values() for i in i]

            searched_list: list[dict] = [i for i in files if name == i['file_name']]

            if len(searched_list) == 0:
                result = "[Linker]并没有找到文件呢~是否文件名输错了？"
                await linker.finish(result)
            elif len(searched_list) == 1:
                file = searched_list[0]
            elif len(searched_list) > 1:
                if info is not None and info <= len(searched_list):
                    file = searched_list[info - 1]
                else:
                    result = f"[Linker]找到了{len(searched_list)}个文件，请输入`/{linker_command} -n 文件名 -i 文件序号`来选择文件"
                    for i in range(len(searched_list)):
                        result += f"\n{i + 1}：上传者{searched_list[i]['uploader_name']}，上传时间" \
                                  + time.strftime('%Y-%m-%d %H:%M:%S',
                                                  time.localtime(searched_list[i]['upload_time']))
                    await linker.finish(result)

            url = await bot.get_group_file_url(group_id=int(event.group_id), file_id=file['file_id'],
                                               bus_id=file['busid'])

            data = {'fname': name}
            url = url.get('url').rpartition("/")[0] + '/?' + urlencode(data).replace('+', '%20')

            result = [f"文件名：{file['file_name']}"
                      f"""\n上传时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file['upload_time']))}"""]
            result.extend(['\n上传者：', MessageSegment(type='at', data={'qq': file['uploader']})])
            result.append(f"\n下载链接：{url}\n")
            # if args["name"] in files:
            #     logger.debug([int(event.group_id), files[args["name"]][0], files[args["name"]][1]])
            #     result = await bot.get_group_file_url(group_id=int(event.group_id),
            #                                           file_id=str(files[args["name"]][0]),
            #                                           bus_id=int(files[args["name"]][1]))
            #     result = "文件名：" + args["name"] + "\n文件类型：" + str(files[args["name"]][1]) + "\n文件id：" + \
            #              files[args["name"]][0] + "\n直链：" + result['url']
            await linker.send(Message(result), at_sender=True)
