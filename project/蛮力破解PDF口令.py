import os,pypdf
#路径
dirctory=open(r'D:\python\project\FunctionTest\处理PDF和Word文档测试目录\dictionary.txt','r')
pdf=open(r'D:\python\project\FunctionTest\处理PDF和Word文档测试目录\encrypted.pdf','rb')

#清洗文件内容
zd=dirctory.read().split('\n')
#进入遍历破解
js=1
for i in range(len(zd)):
    #使用清洗后的数据进行密码破解
    pdfReader=pypdf.PdfReader(pdf)
    if pdfReader.decrypt(zd[i]) != 0:
        print(f'密码破解成功,密码是：{zd[i]}')
        out=0
        break
    elif pdfReader.decrypt(zd[i].lower()) != 0:
        print(f'密码破解成功,密码是：{zd[i].lower()}')
        out=0
        break
    else:
        print(f'密码错误，正在尝试下一条密码！[{js}/{len(zd)}]')
        out=1
        js+=1
if out == 1:
    print('密码破译失败，字典中不存在密码【已尝试小写字段】')

