# How to Convert an EXE File  

> 如何转换 EXE 文件

EXE files are built with a specific operating system in mind.
> 
> EXE 文件是根据特定操作系统构建的。

Decompiling one that's used in Windows would result in many Windows-only compatible files,
> 
> 反编译 Windows 中使用的文件会产生许多仅与 Windows 兼容的文件，

so converting an EXE file to a format that makes it usable on a different platform, like macOS, would be a tedious task.
> 
> 因此将 EXE 文件转换为可在不同平台（如 macOS）上使用的格式将是一项繁琐的任务。

😊😊😊😊😊😊😊😊
## pyinstaller 
### 使用方法
* 命令行：`pyinstaller -F -w fileName`
* GUI：模态框 + [文件操作（路径、处理）](A-按知识点分类/Python/File操作) 

  ### 模态框 ———— [win32ui](https://mhammond.github.io/pywin32/win32ui.html) 
  `from win32ui import CreateFileDialog`
  有好多Crate方法，我只用了`CreateFileDialog`
