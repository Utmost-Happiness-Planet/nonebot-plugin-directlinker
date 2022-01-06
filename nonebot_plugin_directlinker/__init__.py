from nonebot import get_driver, on_message, logger, on_shell_command
from nonebot.adapters.cqhttp import Bot, GroupMessageEvent, MessageSegment
from nonebot.typing import T_State
from nonebot.rule import ArgumentParser
from collections import deque

linker_group = get_driver().config.linker_group

linker_parser = ArgumentParser(add_help=False)
linker_parser.add_argument("-h", "--help", dest="help", action="store_true")
linker_parser.add_argument("-n", "--name", dest="name")

linker = on_shell_command("link", parser=linker_parser, priority=1)

help_text = """Manual of 群文件直链提取器
-n | --name     文件名*
"""


@linker.handle()
async def link(bot: Bot, event: GroupMessageEvent, state: T_State):
    gid = str(event.group_id)
    if gid in linker_group:
        args = vars(state.get("args"))
        # logger.debug(args["name"])
        if args["help"]:
            await linker.finish(help_text)
        else:
            if args["name"] is None:
                await linker.finish("[Linker]不输入文件名可提取不了直链哦~")
            else:
                await bot.send(event, "[Linker]处理中，请稍后…")
                root = await bot.get_group_root_files(group_id=int(event.group_id))
                folders = root.get("folders")
                files = {}
                for i in root.get("files"):
                    files[i["file_name"]] = (i["file_id"], i["busid"])
                # 广度优先搜索
                d = deque()
                d.extend([i["folder_id"] for i in folders])
                while d:
                    _ = d.popleft()
                    logger.debug("下一个搜索的文件夹：" + _)
                    root = await bot.get_group_files_by_folder(group_id=int(event.group_id), folder_id=_)
                    folders = root.get("folders")
                    for i in root.get("files"):
                        files[i["file_name"]] = (i["file_id"], i["busid"])
                    if folders:
                        d.extend([i["folder_id"] for i in folders])

                logger.debug("共扫描出 " + str(len(files)) + " 个文件")

                if args["name"] in files:
                    logger.debug([int(event.group_id), files[args["name"]][0], files[args["name"]][1]])
                    result = await bot.get_group_file_url(group_id=int(event.group_id), file_id=str(files[args["name"]][0]), bus_id=int(files[args["name"]][1]))
                    result = "文件名：" + args["name"] + "\n文件类型：" + str(files[args["name"]][1]) + "\n文件id：" + files[args["name"]][0] + "\n直链：" + result['url']
                else:
                    result = "[Linker]并没有找到文件呢~是否文件名输错了？"
                await linker.finish(result)
