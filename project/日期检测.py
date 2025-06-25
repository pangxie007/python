import re
rule=re.compile(r'''
                (\d{1,2})      #匹配日期
                /
                (\d{1,2})      #匹配月份
                /
                (\d{4})        #匹配年份
                ''',re.VERBOSE)
rule_mont=re.compile(r'4|6|9|11')
#元组中的数据是不可以被修改和删除的，所以不适合 但是列表配合字符可以很好进行使用操作
#如果日期和月份是1个数 则在前面填0
shuju=rule.findall('30/11/2025 3/1/2025 29/2/2000 31/4/2000')
#将元组装换成列表
date=[]
for i in range(len(shuju)):
    date.append(list(shuju[i]))
# 检测日期和月份是否只有一位数，是就在前面添加0
for i in range(len(date)):
    for j in range(len(date[i])-1):
        if len(date[i][j])<2:
            date[i][j]=f"{int(date[i][j]):02d}"     #这里使用的是【字符串格式化】
print(date)
#检测是否为有效日期
#判断是否是润年 如果是闰年 4，6，9，11月有30天 2月有29天 其余月份31天 如果不是闰年 4，6，9，11月有30天 2月有28天 其余月份31天
for i in range(len(date)):
    if int(date[i][2])%4==0:
        print(f'{date[i]}是润年')
        if int(date[i][1])==2 and int(date[i][0])>29:
            print('日期错误，闰年2月份只有29天')
    else:
        print(f'{date[i]}不是润年')
        if int(date[i][1])==2 and int(date[i][0])>28:
            print('日期错误，2月份只有28天')

    if int(date[i][1])==4 and int(date[i][0]) > 30:
        print('日期错误，4，6，9，11月有30天')
    elif int(date[i][1])!=2 and int(date[i][0]) >31:
        print('日期错误，除4，6，9，11，2 以外的月份都是31天')