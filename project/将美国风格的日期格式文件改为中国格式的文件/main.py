import os,re,shutil
#正则表达式
rule=re.compile(r'(\d)-(\d)-(\d\d\d\d)(.*)$')
rule_zh=re.compile(r'(\d\d\d\d)-(\d)*-(\d)*(.*)$')
#列出文件，获取文件名
path=r"D:\python\project\project\将美国风格的日期格式文件改为中国格式的文件\file_data"
fileNameList=os.listdir(f"{path}")
print(fileNameList)
content_ture=[]
#判断是否是美国风格,将风格过滤
for i in range(len(fileNameList)):
    content=rule_zh.search(fileNameList[i])
    if content:
        print(content.group())
        content_ture.append(content.group())
        # 重命名文件
        shutil.move(rf"{path}\{content.group()}",rf"{path}\{content.group(1)}-{content.group(3)}-{content.group(2)}{content.group(4)}")
        # content_oute.append(f"{content.group(3)}-{content.group(2)}-{content.group(1)}{content.group(4)}")
print(f'匹配到的风格的日期有：{content_ture}')