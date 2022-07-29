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

1. 配合下载器高速下载（本来速度就不慢）
2. 分享给不在群里的人（转发功能了解一下）

### 用法

配置文件`.env.*`中添加：

```python
linker_group=["<QQ群号>"]  # 启用插件的群
```

### 插件语法

```python
/link -h|--help  # 获取帮助
/link -n|--name <文件名>  # 获取文件直链
```

### 致谢

感谢我自己，虽然被人说该插件毫无卵用，我还是把它开发出来了。
