'''这个脚本的功能是将剪切板中的内容加工处理之后以空格的方式进行分隔
然后在每行开头加入一个 【*】 来标识，最后加工后的文本返回到剪切板'''

import pyperclip

# 将剪切板内容给strPool变量进行存储
strPool = pyperclip.paste()
# 文本处理区域
strList = strPool.split()  # 将文本以某种格式锚点装换成列表形式存储【默认是空格方式分隔】

print(strList)
for i in range(len(strList)):
    strList[i] = '*' + strList[i]
    print(strList[i])
strPool='\n'.join(strList) #使用join方法将列表中的字符串连接起来复制给 strPool
# 输出变量
pyperclip.copy(strPool)