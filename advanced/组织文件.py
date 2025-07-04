"""shutil模块，可以在python程序中复制、移动、重命名和删除文件"""
#复制文件和文件夹 【shutil.copy shutil.copytree】
    # import shutil
    # shutil.copy(r"D:/python/project/FunctionTest/PengXvsb.py",r"D:/python/project/FunctionTest/组织文件测试")
    # shutil.copy(r"D:/python/project/FunctionTest/组织文件测试/PengXvsb.py",r"D:/python/project/FunctionTest/组织文件测试/test.pyw")

    # shutil.copytree(r"/FunctionTest/a", r"D:/python/project/FunctionTest/组织文件测试/b")

#文件和文件夹的移动与重命名【shutil.move】
    # import shutil
    #移动
    # shutil.move(r"D:/python/project/FunctionTest/a",r"D:/python/project/FunctionTest/组织文件测试/")
    #重命名
    # shutil.move(r"D:/python/project/FunctionTest/组织文件测试/a/1",r"D:/python/project/FunctionTest/组织文件测试/a/2")

#永久删除文件和文件夹 【os.unlink os.rmdir shutil.rmtree】
    # import os,shutil,pathlib
    # for filename in pathlib.Path(r"D:\python\project\FunctionTest\组织文件测试\删除文件").glob('*.txt'):
    #     print(filename)
        # os.unlink(filename)

    #目录中有文件删除不了
    # os.rmdir(r"D:\python\project\FunctionTest\组织文件测试\删除文件")
    #即使目录中有文件也删除
    # shutil.rmtree(r"D:\python\project\FunctionTest\组织文件测试\删除文件")

#用send2trash模块安全地删除 使用这个三方模块的原因是python自带的 shutil.rmtree函数删除文件不能追回
    # import send2trash
    # #创建一个文件 写入内容
    # baconFile=open('bacon.txt','a')
    # baconFile.write('这个是一个测试文件！！！')
    # baconFile.close()
    # #删除上面创建的文件，删除之后的文件存在于电脑的回收站中
    # send2trash.send2trash('bacon.txt')

#遍历目录树  【os.walk os.listdir】
    # import os
    # for folderName,subfolders,filenames in os.walk(r"D:/python/project/FunctionTest/遍历目录数测试目录"):
    #     print(f'文件夹有:{folderName}')
    #     print(f'子目录有:{subfolders}')
    #     print(f'文件有:{filenames}')

#用zipfile模块压缩文件
#读取zip文件
    # import zipfile
    # exampleZip=zipfile.ZipFile(r"D:/python/project/FunctionTest/组织文件测试/Zip_file.zip")
    # print(exampleZip)
    # print(type(exampleZip))
    # print(exampleZip.namelist())
    #
    # zipFileInfo=exampleZip.getinfo('zip_1.txt')
    # #file_size表示文件原本大小 compress_size表示压缩后的大小
    # print(zipFileInfo.file_size)
    # print(zipFileInfo.compress_size)
    #
    # exampleZip.close()

#从zip文件中解压缩
    # import zipfile
    # exampleZip=zipfile.ZipFile(r"D:\python\project\FunctionTest\组织文件测试\zip_file.zip")

    # #将压缩包解压到指定路径下
    # exampleZip.extractall(r"D:\python\project\FunctionTest\组织文件测试")
    # exampleZip.close()

    #解压指定文件
    # exampleZip.extract('zip_1.txt',r"D:\python\project\FunctionTest\组织文件测试")

#创建和添加到zip文件
    # import zipfile
    # newZip=zipfile.ZipFile(r"D:\python\project\FunctionTest\组织文件测试\new.zip",'w')
    # newZip.write(r"D:\python\project\FunctionTest\组织文件测试\PengXvsb.py",'PengXvsb.py',compress_type=zipfile.ZIP_DEFLATED)
    # #当你以'a'（追加模式）打开 ZIP 文件时，需要确保之前的写入操作已经通过newZip.close()或with语句正确关闭。否则，文件可能处于不一致状态，导致追加失败
    # newZip.close()
    # newZip=zipfile.ZipFile(r"D:\python\project\FunctionTest\组织文件测试\new.zip",'a')
    # newZip.write(r"D:\python\project\FunctionTest\组织文件测试\test.pyw",'test.pyw',compress_type=zipfile.ZIP_DEFLATED)
    # print(newZip.namelist())