import pyperclip,re
#文本入栈到剪切板，并将内容传递给data变量
data=pyperclip.paste()
# print(type(data))
#正则表达式处理文字
#电话号码处理
rule_phone=re.compile(r'''
                    \d{3,4}      #匹配三位或者四位区号
                    -            #匹配分隔符
                    \d{7,8}      #匹配后七位或者八位本地号
                    ''',re.VERBOSE)
jieguo_phone=rule_phone.findall(data)
#邮箱处理
rule_email=re.compile(r'''
                    [a-zA-Z0-9._%+-]+    # 用户名部分（允许字母、数字和特殊符号）
                    @                    # @符号
                    [a-zA-Z0-9-]+        # 域名的第一部分（如gmail、126等，允许数字）
                    (?:\.[a-zA-Z]{2,})+  # 顶级域名（如.com）或多级域名（如.co.uk）
                      ''',re.VERBOSE)
jieguo_email=rule_email.findall(data)
#总合处理后的数据
# print("过滤到的电话号码：")
for i in range(len(jieguo_phone)):
    print(jieguo_phone[i])

# print("过滤到的邮箱：")
for i in range(len(jieguo_email)):
    print(jieguo_email[i])

#将处理完毕的数据传输到剪切板
result=jieguo_phone+jieguo_email
# print(result)
if len(result)>0:
    pyperclip.copy('\n'.join(result))
else:
    print('复制的文本中没有可以匹配到的电话和邮箱')