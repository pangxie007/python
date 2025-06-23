#不用正则表达式来查找文本模式
    # def isPhoneNumber(text):
    #     if len(text)==12 and text[:3].isdecimal() and text[4:7].isdecimal() and text[-4:].isdecimal() and text[3] =='-' and text[7] =='-':
    #         return True
    #     return False
    # print(isPhoneNumber('123-456-7890'))
    # strin='这是一串字符串 我在这里嵌入一串电话号码测试函数能不能查找出来我的电话号码是：111-333-4444，看函数能不能查找到'
    # for i in range(len(strin)):
    #     check=strin[i:i+12]
    #     if isPhoneNumber(check):
    #         print(f'找到电话号码，电话号码是{check}')

#使用正则表达式查找文本模式
    #创建对象，匹配Gegex对象
        # import re 
        # phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        # mo=phoneNumRegex.search('我的电话号码是:222-222-2222。测试能否找到')
        # print('我的电话号码是：' + mo.group())
        # print(type(phoneNumRegex))
        # print(type(mo))

#用正则表达式匹配更多模式
    #利用括号分组
        # import re
        # pheoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
        # mo=pheoneNumRegex.search('my Phone is 555-444-33333')
        # print(mo.group(1))
        # print(mo.group(2))
        # print(mo.groups())
        # a,b=mo.groups()
        # print(a)
        # print(type(a))
        # print(b)
        # print(type(b))

        # import re
        # pheoneNumRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
        # mo=pheoneNumRegex.search('my Phone is (111)-444-3333')
        # print(mo.group(1))
        # print(mo.group(2))

    #用管道匹配多个分组
        # import re
        # herRegex=re.compile(r'湖北|荆州')
        # mo=herRegex.search('我是湖北人')
        # print(mo.group())
        # mo1=herRegex.search('我是荆州人')
        # print(mo1.group())
        # barRegex=re.compile(r'湖北(荆州|武汉|孝感|黄石)')
        # mo=barRegex.search('我是湖北荆州人')
        # print(mo.group())
        # mo1=barRegex.search('我是湖北武汉人')
        # print(mo1.group())
        # print(mo.group(1))

    #用问号实现可选匹配
        # import re
        # batRegex=re.compile(r'湖北(荆州)?人')
        # mo=batRegex.search('我是湖北人')
        # print(mo.group())
        # mo1=batRegex.search('我是湖北荆州人')
        # print(mo1.group())
        # mo2=batRegex.search('我是湖北人，你是湖北荆州人吗')
        # print(mo2.group())

        # import re
        # phoneNumRegex=re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
        # mo=phoneNumRegex.search('我的电话号码是：222-222-2222, 测试是否能过滤')
        # print(mo.group())
        # print(mo.group(1))
        # print(mo.group(2))
        # mo1=phoneNumRegex.search('我的电话号码是：222-2222, 测试是否能过滤')
        # print(mo1.group())

    #用星号匹配零次或多次
        # import re
        # rule=re.compile(r'1(0)*元钱')
        # shuju=rule.search('我现在有1元钱')
        # print(shuju.group())
        # shuju=rule.search('我现在有10元钱')
        # print(shuju.group())
        # shuju=rule.search('我现在有100000000元钱')
        # print(shuju.group())

    #用加号匹配一次或多次
        # import re
        # batRegex=re.compile(r'我是花东方，是大(笨)+🐖')
        # try:
        #     shuju=batRegex.search('我是花东方，是大🐖')
        #     print(shuju.group())
        # except AttributeError:
        #     print('没有匹配到数据')
        # shuju=batRegex.search('我是花东方，是大笨🐖')
        # print(shuju.group())
        # shuju=batRegex.search('我是花东方，是大笨笨🐖')
        # print(shuju.group())
        # shuju=batRegex.search('我是花东方，是大笨笨笨笨🐖')
        # print(shuju.group())

    #用花括号匹配特定次数
        # import re
        # haRegex=re.compile(r'1(0){3}')
        # try:
        #     shuju=haRegex.search('我有1块钱')
        #     print(shuju.group())
        # except AttributeError:
        #     print('没有匹配到')
        # shuju=haRegex.search('我有1000块钱')
        # print(shuju.group())

        # haRegex=re.compile(r'1(0){3,5}')
        # shuju=haRegex.search('我有10000块钱')
        # print(shuju.group())
        # shuju=haRegex.search('我有1000000块钱')
        # print(shuju.group())

        # haRegex=re.compile(r'1(0){3,}')
        # shuju=haRegex.search('我有10000块钱')
        # print(shuju.group())

        # haRegex=re.compile(r'1(0){,5}')
        # shuju=haRegex.search('我有10000块钱')
        # print(shuju.group())

    #贪心和非贪心匹配
        # import re
        # haRegex=re.compile(r'1(0){3,5}')        #贪心匹配
        # shuju=haRegex.search('我有10000000块现金')
        # print(shuju.group())

        # haRegex=re.compile(r'1(0){3,5}?')       #惰性匹配
        # shuju=haRegex.search('我有10000000块现金')
        # print(shuju.group())

#findall()方法
    # import re
    # phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # mo=phoneNumRegex.search('私人电话：111-222-3333，公司电话：444-555-6666')
    # print(mo.group())
    # mo1=phoneNumRegex.findall('私人电话：111-222-3333，公司电话：444-555-6666')
    # print(mo1)  #findall()方法返回的是一个字符串列表
    # print(type(mo1))
    # print(type(mo1[0]))

    # #如果正则表达式中有分组，那么findall方法会返回一个元组列表
    # phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    # mo=phoneNumRegex.findall('私人电话：111-222-3333，公司电话：444-555-6666')
    # print(mo)
    # print(type(mo))
    # print(type(mo[0]))

#字符分类
        # \d 0~9的任何数字
        # \D 除了0~9的任何字符
        # \w 任何字母、数字或下划线
        # \W 除了字母、数字和下划线
        # \s 任何空白字符
        # \S 除了空白字符
        # . 除了换行符之外的任何字符
        # \b 一个单词边界
        # \B 除了单词边界之外的任何字符
        # ^ 以...开始
        # $ 以...结束
    # import re
    # rule=re.compile(r'\d+\s\w+')
    # shuju=rule.findall('1 a,2 c,3 bb,4 qwe,5 123,6 _@,6 66,7777, 888')
    # print(shuju)

#建立自己的字符分类
    # import re
    # #使用方括号定义字符分类
    # rule=re.compile(r'[aeiouAEIOU]')
    # print(rule.findall('wo yao qu shui jiao'))
    # #使用短横线表示字母或数字的范围
    # rule=re.compile(r'[0-9]')
    # print(rule.findall('wo yao qu shui jiao 12 123 123'))
    # #非字符类 等同于取反操作 不会匹配规则中字符串的类型
    # rule=re.compile(r'[^aeiouAEIOU]')
    # print(rule.findall('aaa eee iii ddd'))
    # #对比不加方括号定义的字符分类 可以发现默认就是匹配全部长度 方括号会对单一长度进行匹配
    # rule=re.compile(r'[a]')
    # print(rule.findall('wo yao qu shui jiao'))
    # rule=re.compile(r'[ao]')
    # print(rule.findall('wo yao qu shui jiao'))

#插入字符和美元字符
    # import re
    # #使用插入符号【^】会从匹配字符串的开头开始匹配
    # rule=re.compile(r'^你好')
    # shuju=rule.search('你好我叫花花')
    # print(shuju.group())
    # shuju=rule.search('我是花花')
    # print(shuju==None)
    # #使用美元字符【$】会从匹配字符串的结尾开始匹配
    # rule=re.compile(r'\d$')
    # shuju=rule.search('你好我叫花花,我今年22')
    # print(shuju.group())
    # shuju=rule.search('你好我叫花花,我今年二十二')
    # print(shuju==None)
    # #同时使用插入、美元字符，表明整个匹配字符串必须按照规则进行匹配
    # rule=re.compile(r'^\d+$')
    # shuju=rule.search('123')
    # print(shuju.group())
    # shuju=rule.search('123asdasd')
    # print(shuju==None)

#通配字符【匹配换行符之外的所有字符】
    # import re
    # rule=re.compile(r'.好')
    # shuju=rule.findall('你好 我好 他好 都不好')
    # print(shuju)
    # shuju=rule.findall('你好 .好 1好 #好  好 \n好 \t好')
    # print(shuju)

    #用点-星匹配所有字符
        # import re
        # rule=re.compile(r'.*')
        # shuju=rule.search('这是一个安静的晚上')
        # print(shuju.group())
        # shuju=rule.search('asdwsdwafw')
        # print(shuju.group())
        # shuju=rule.search(' @#$@$@!@$$')
        # print(shuju.group())

        # rule=re.compile(r'姓:(.*)名:(.*)')
        # shuju=rule.search('你好我叫花东方，姓:花名:东方')
        # print(shuju.group())
        # print(shuju.group(1))
        # print(shuju.group(2))
        # #贪心模式
        # rule=re.compile(r'<.*>')
        # shuju=rule.search('<今天星期一>天气真好>')
        # print(shuju.group())
        # #非贪心模式
        # rule=re.compile(r'<.*?>')
        # shuju=rule.search('<今天星期一>天气真好>')
        # print(shuju.group())

    #用句点字符匹配换行符
        # import re
        # rule=re.compile(r'.*')
        # print(rule.search('这是一个安静的晚上\n我想和你打打电话').group())

        # rule=re.compile(r'.*',re.DOTALL)
        # shuju=rule.search('这是一个安静的晚上\n我想和你打打电话')
        # print(shuju.group())

#不区分大小写的匹配
    # import re
    # rule=re.compile(r'AaCup')
    # print(rule.search('Aacup'))
    # print(rule.search('AaCup'))

    # rule=re.compile(r'AaCup',re.I)
    # print(rule.search('AACUP').group())

#用sub方法替换字符串
    # import re
    # rule=re.compile(r'绝望的机长 \w+')
    # print(rule.search('绝望的机长 破碎的家庭 破碎的梦想'))
    # print(rule.sub('哈哈哈','绝望的机长 破碎的家庭 破碎的梦想 绝望的机长 破碎的家庭 没有人的地方'))

    # rule=re.compile(r'机长(\w)\w+')
    # print(rule.search('小学机长A没有起飞,大学机长B没有起飞,研究生机长C没有起飞,博士机长D没有起飞'))
    # print(rule.sub(r'\1****','小学机长A没有起飞,大学机长B没有起飞,研究生机长C没有起飞,博士机长D没有起飞'))

#管理复杂的正则表达式
    # import re
    # rule=re.compile(r'''(
    #                     (\d{3}|\(\d{3}\))?              #匹配前三个区号数字
    #                     (\s|-|\.)?                      #匹配区号和电话号码之间的分隔符
    #                     \d{3}                           #匹配中间三个数字
    #                     (\s|-|\.)                       #匹配区号和电话号码之间的分隔符
    #                     \d{4}                           #匹配最后四个数字
    #                     (\s*(ext|x|ext.)\s*\d{2,5})?    #匹配可选的扩展信息
    #                 )''',re.VERBOSE)
    # print(rule.search('my phone is : (111)-222-3333'))

#组合使用re.IGNORECASE和re.DOTALL和re.VERBOSE
    # import re
    # rule=re.compile('''
    #                     foo    #匹配foo
    #                 ''',re.IGNORECASE|re.DOTALL|re.VERBOSE)
    # print(rule.search('FOO\naS'))

    # rule=re.compile('''
    #                     foo.*    #匹配foo
    #                 ''',re.IGNORECASE|re.DOTALL|re.VERBOSE)
    # print(rule.search('FOO\nNMAS'))