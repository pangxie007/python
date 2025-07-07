"""
这个脚本的使用场景是；我在一个目录下面作业，因为害怕文件丢失，又不想频繁的进行手动备份，所以需要手写一个脚本用来定时备份
"""
import os,datetime,zipfile
def backupToZip(folder,backfolder):
    #获取时间信息
    now = datetime.datetime.now()
    #获取绝对路径
    folder=os.path.abspath(folder)
    bf=os.path.abspath(backfolder)
    #定义压缩包名称
    zipName=(f"{os.path.basename(folder)}_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.zip")
    #创建压缩包
    createZip=zipfile.ZipFile(rf"{bf}\{zipName}",'w')
    #遍历目录树 将文件写入压缩包
    '''原理利用了zipfile会自己创建路径的文件夹'''
    for folderName, subfolders, filenames in os.walk(rf"{folder}"):
        for file in filenames:
            file_path=os.path.join(folderName,file)
            arcname=os.path.relpath(file_path,os.path.dirname(rf"{folder}"))
            createZip.write(file_path,arcname)
        for dir in subfolders:
            dir_path=os.path.join(folderName,dir)
            arcname=os.path.relpath(dir_path,os.path.dirname(rf"{folder}"))
            createZip.write(dir_path,arcname)
    # createZip.write(f"{folder}",,compress_type=zipfile.ZIP_DEFLATED)


backupToZip(r"D:\python\project\project\将一个文件夹备份到一个zip文件\WorkShop",r"D:\python\project\project\将一个文件夹备份到一个zip文件\backfolder")