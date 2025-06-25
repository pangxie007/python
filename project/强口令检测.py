import re
rule_len=re.compile(r'\S{8,}')          #长度测试
rule_dxx=re.compile(r'[a-zA-Z]')       #大小写测试
rule_num=re.compile(r'\d+')             #数字测试
def check_passwd(passwd):
    shuju=rule_len.search(f'{passwd}')
    print(f'{shuju.group()}通过长度测试')
    shuju=rule_dxx.search(f'{passwd}')
    print(f'{shuju.group()}通过大小写测试')
    shuju=rule_num.search(f'{passwd}')
    print(f'{shuju.group()}通过数字测试')
#数据获取
a=input('请输入设置的密码:')
#数据送检
check_passwd(a)