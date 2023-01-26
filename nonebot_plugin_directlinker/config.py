from nonebot import get_driver, logger

config = get_driver().config.dict()

if 'linker_group' not in config:
    logger.warning('[直链提取] 未发现配置项 `linker_group` , 采用默认值: []')
if 'linker_command' not in config:
    logger.warning('[直链提取] 未发现配置项 `linker_command` , 采用默认值: "link"')


linker_group = config.get('linker_group', [])
linker_command = config.get('linker_command', "link")
