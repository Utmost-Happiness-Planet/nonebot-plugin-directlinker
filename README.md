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

### 演示

假设有一群文件为以下目录结构：

***注意：在腾讯的群文件中，允许在同一个文件夹下存在两个文件不同，但是文件名相同的文件***

```text
│ foo.txt
| bar.txt
└─Folder1
    bar.txt
    bar.txt
```

在群文件根目录有一个`bar.txt`，在`Folder1`目录下有两个文件`bar.txt`和`foo.txt`。

`/<linker_command> -h`
`/<linker_command> --help`

输出
  
```text
Manual of 群文件直链提取器
-n | --name     文件名.*
-i | --info     文件序号 
-p | --path     文件路径
例：/link -n 文件名.exe
```

#### 提取文件直链

`/<linker_command> -n <文件名>`
`/<linker_command> --name <文件名>`

对于上述目录结构，输入`/<linker_command> -n foo.txt`，会直接输出其直链，这是因为在群文件中有且只有一个`foo.txt`。

但同样对于`bar.txt`，则会输出以下内容：

```text
[Linker]找到了多个文件，请输入`/link -n 文件名.* -f 文件序号`来选择文件
1：上传者 * ，上传时间****-**-** **:**:**
2：上传者 * ，上传时间****-**-** **:**:**
```

在群文件中存在两个文件名一样的`bar.txt`，我们无法直接提取其直链，需要指定某个文件。

`/<linker_command> -n <文件名> -i <文件序号>`
`/<linker_command> --name <文件名> --info <文件序号>`

或者，在同文件夹内文件不重复的情况下，可以使用文件路径来提取直链。

对于文件路径，在群文件根目录下请使用`/`，在子目录下请直接使用子目录名，如`Folder`。

`/<linker_command> -n <文件名> -p <文件路径>`
`/<linker_command> --name <文件名> --path <文件路径>`
