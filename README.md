<div align="center">

  # DirectLinker
  
  ✨ 一个基于 [NoneBot2](https://github.com/nonebot/nonebot2) 的插件，用于提取QQ群文件的直链 ✨
  
</div>

<p align="center">
  
  <a href="https://github.com/ninthseason/nonebot-plugin-directlinker/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-GPL3.0-informational">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot-v2-green">
  </a>
  
  <a href="https://github.com/Mrs4s/go-cqhttp">
    <img src="https://img.shields.io/badge/go--cqhttp-v1.0.0-red">
  </a>
  
  <a href="">
    <img src="https://img.shields.io/badge/release-v1.0-orange">
  </a>
  
</p>

### 用途

1. 配合下载器高速下载
2. 分享给不在群里的人

### 用法

配置文件`.env.*`中添加：

```python
COMMAND_START=["/", ""]  # 别忘了设置指令前缀，这里只是提醒一下，如果你不知道这个有什么用，请阅读nonebot文档

linker_group=["<QQ群号>"]  # 启用插件的群
linker_command="link" # 设置插件触发命令（默认`link`）
```

### 插件语法

```python
/<link_command> -h|--help  # 获取帮助
/<link_command> -n|--name <文件名>  # 获取文件直链
```
