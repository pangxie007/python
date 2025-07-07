""""
这个项目的函数会作为工具去使用，由一个 srcPath 和 destPath 进行路径传入，然后打印出获得到的数据内容
"""
import os
def traverse(srcPath):
    file_path=[]
    dir_path=[]
    print('目录中的元素有:')
    for folderName,subfolders,filenames in os.walk(srcPath):
        print(folderName,subfolders,filenames)
        for file in filenames:
            file_path.append(os.path.join(folderName,file))
        for folder in subfolders:
            dir_path.append(os.path.join(folderName,folder))
    print(f'目录中的文件有：{file_path}')
    print(f'目录中的子目录有：{dir_path}')

srcPath = r"D:\python\project\FunctionTest\遍历目录数测试目录"
traverse(srcPath)