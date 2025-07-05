"""遍历目录树，查找特别大的文件或文件夹，比如超过了10MB的文件 将其删除"""
import os
def traverse(srcPath):
    # print('目录中的元素有:')
    for folderName,subfolders,filenames in os.walk(srcPath):
        # print(folderName,subfolders,filenames)
        for file in filenames:
            file_path.append(os.path.join(folderName,file))
        for folder in subfolders:
            dir_path.append(os.path.join(folderName,folder))
    # print(f'目录中的文件有：{file_path}')
    # print(f'目录中的子目录有：{dir_path}')
    return file_path,dir_path

file_path=[]
dir_path=[]
srcPath=r"D:\python\project\FunctionTest\遍历目录数测试目录"
traverse(srcPath)

for i in file_path:
    fileSize=os.path.getsize(i)
    print(fileSize)
    if fileSize >= 50:
        print(i)
        os.unlink(i)