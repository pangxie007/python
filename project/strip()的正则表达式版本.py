import re
#正则表达式
rule=re.compile(r'^\s+|\s+$')
def renew_strip(valu1,valu2):
    if valu2 == 'None':
        shuju=rule.sub('',valu1)
        print(shuju)
    else:
        shuju=re.sub(f'{b}','',valu1)
        print(shuju)
#字符接收

a=input("输入要处理的字符串：")
b=input('输入指定删除的字符,如果没有则输入None:')
#字符处理
renew_strip(a,b)