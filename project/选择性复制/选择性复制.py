import os,shutil,re,pprint
#定义正则表达式匹配规则
rule=re.compile(r'.*.png$|.*.pdf$')
#遍历目录
file=[]
outdate=[]
path= r"D:\python\project\FunctionTest\遍历目录数测试目录"
destPath=r"D:\python\project\project\选择性复制\destfile"
#获取目录树中的所有文件的绝对路径
for folderName,subfolders,filenames in os.walk(path):
    for i in filenames:
        file.append(os.path.join(folderName,i))
pprint.pprint(file)
#使用正则表达式对文件进行筛选 文件的绝对路径也筛选完毕
for i in file:
    if rule.search(os.path.basename(i)):
        outdate.append(i)
        print(f"满足匹配规则的有：{os.path.basename(i)}")
pprint.pprint(outdate)
#将筛选后的文件复制到新文件夹中
for i in outdate:
    shutil.move(rf"{i}",rf"{destPath}")