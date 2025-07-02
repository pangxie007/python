#打开目录中的所有txt文件
import os,re
rule=re.compile(r'.*txt$')
rule_sjgl=re.compile(r'.*游泳.*')

txtFile=os.listdir(r'D:\python\project\FunctionTest\正则表达式查找测试')

txtList=[]
for i in range(len(txtFile)):
    if rule.search(txtFile[i]) is not None:
        # print(rule.search(txtFile[i]).group())
        txtList.append(rule.search(txtFile[i]).group())

print(txtList)

for i in range(len(txtList)):
    file_content=open(rf'D:\python\project\FunctionTest\正则表达式查找测试\{txtList[i]}',encoding='utf-8')
    print(rule_sjgl.search(file_content.read()).group())