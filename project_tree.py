import os

def generate_tree(startpath, ignore_dirs=None, ignore_files=None):
    """
    生成项目目录树
    
    参数:
        startpath: 项目根目录路径
        ignore_dirs: 要忽略的目录列表
        ignore_files: 要忽略的文件列表
    """
    if ignore_dirs is None:
        ignore_dirs = ['.git', '__pycache__', 'venv', '.idea']
    if ignore_files is None:
        ignore_files = ['.gitignore', '.DS_Store']
    
    output = []
    
    for root, dirs, files in os.walk(startpath):
        # 过滤掉要忽略的目录
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        # 计算当前层级
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * level
        
        # 添加目录名
        dir_name = os.path.basename(root)
        if level > 0:
            output.append(f'{indent[:-4]}├── {dir_name}/')
        else:
            output.append(f'{dir_name}/')
        
        # 添加文件
        sub_indent = '│   ' * (level + 1)
        for file in sorted(files):
            if file not in ignore_files:
                output.append(f'{sub_indent[:-4]}├── {file}')
    
    # 写入文件
    with open('projectStructure.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    return '\n'.join(output)

if __name__ == '__main__':
    # 获取当前目录作为起始路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    
    # 生成目录树并打印
    tree = generate_tree(current_path)
    print(tree) 