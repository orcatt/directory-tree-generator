# Directory Tree Generator

`directory-tree-generator` 是一个简单的 Python 脚本，用于生成项目的目录树，并以 Markdown 格式输出。你可以使用它来快速查看项目结构或生成项目的目录树文档。

## 特性

- 递归遍历项目文件夹，并生成目录树。
- 支持忽略指定的目录和文件，例如 `.git`、`__pycache__`、`.gitignore` 等。
- 输出目录树为 Markdown 格式，方便与文档一同使用。

## 安装与使用

### 安装

直接克隆仓库或下载 `generate_tree.py` 文件：

```bash
git clone https://github.com/orcatt/directory-tree-generator.git
cd directory-tree-generator
```

### 使用方法

将 generate_tree.py 文件放置在你的项目根目录下。

运行脚本，脚本会自动扫描当前目录的结构并生成 Markdown 格式的目录树。

```bash
python generate_tree.py
```

生成的目录树会保存为 projectStructure.md 文件，并在控制台中打印。

## 参数说明

startpath: 项目根目录路径，默认为当前目录。

ignore_dirs: 要忽略的目录列表，例如 .git、__pycache__ 等，默认为 ['.git', '__pycache__', 'venv', '.idea']。

ignore_files: 要忽略的文件列表，例如 .gitignore、.DS_Store，默认为 ['.gitignore', '.DS_Store']。

## 贡献

欢迎贡献代码！如果你有好的功能想法或发现了 bug，欢迎提交 issue 或者 pull request。

