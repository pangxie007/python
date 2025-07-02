import re,pyinputplus
#创建文件，写入文件内容
myFile=open('fktc.txt','w',encoding='utf-8')
myFile.write('这是一个形容词的名词，我们副词一起动词去北京')
#读取文件
myFile=open('fktc.txt','r',encoding='utf-8')
content=myFile.read()
print(content)
# print(type(content))
#使用pyinputplus进行文本输入，并将输入文本替换到关键字中

#对文件内容进行过滤，找出关键字
rule=re.compile(r'名词')
content=(rule.sub(pyinputplus.inputStr('输入名词:'),content))
print(content)

rule=re.compile(r'形容词')
content=(rule.sub(pyinputplus.inputStr('输入形容词:'),content))
print(content)

rule=re.compile(r'副词')
content=(rule.sub(pyinputplus.inputStr('输入副词:'),content))
print(content)

rule=re.compile(r'动词')
content=(rule.sub(pyinputplus.inputStr('输入动词:'),content))
print(content)

myFile=open('fktc.txt','w',encoding='utf-8')
myFile.write(content)
myFile=open('fktc.txt','r',encoding='utf-8')
print(myFile.read())