#处理字符串
'''
    使用单引号时python的处理规则很简单，单引号开头，单引号结尾，中间内容就是字符串内容，如果单引号出现位置不规范则会报错 SyntaxError
    在某些特定环境下必须使用单引号来表示一个句子的意思的情况下，可以使用双引号、转义字符来实现
'''
    #字符串字面量
        #双引号 
            # # print('This's her') #SyntaxError
            # print("This's her")
        #转义字符
            # print('This\'s her')
        #原始字符串 原始字符串会会忽略转义字符
            # print(r'This\'s her')
        #三重引号的多行字符串
            # print('''三重引号字符串不会在乎
            # 引号
            # 空格
            # 转义字符\'s 
            # \n
            # \t
            # \\
            # 这些都被三重引号字符忽略了，被认为是输出的一部分''')
        #多行注释 它们实际上是字符串字面量，而不是真正的注释，当三引号字符串前面有缩进时，这个字符串会成为代码的一部分，而不是被忽略的注释。
        # '''
        # asdasd
        # \n
        # \t
        # \\
        # 多行注释
        # '''

        # """
        # asdasd
        # \n
        # \t
        # \\
        # 多行注释
        # """

    #字符串索引和切片
        # spam='Hello World!'
        # for i in range(len(spam)):
        #     print(spam[i])
        # print(spam[0:5])
        # print(spam[-1])
        # print(spam[1:])
        # print(spam[:4])
    
    #字符串的 in 和 not in 操作符
        # print('Hello' in 'Hello World!')
        # print('Hello' not in 'Hello World!')
        # print(' ' in 'Hello World!')
        # print('hello' in 'Hello World!')    #区分大小写

#将字符串放入其他字符串
    # spam='Hello'
    # number=1000
    # print('我说' + spam +',你猜我今年多少岁？'+ str(number))
    # print('我说%s,你猜我今年多少岁？%s'%(spam,number))
    # print(f'我说{spam},你猜我今年多少岁？{number}')

#有用的字符串方法
    #字符串方法 upper() lower() isupper() islower()
        # spam='Hello World!'
        # SPAM=spam.upper()   #upper()方法会将字符串全部转换成大写
        # print(SPAM)
        # SPAM=spam.lower()
        # print(SPAM)         #lower()方法会将字符串全部转换成小写

        # print(spam.isupper())       #isupper()方法判断字符串是否全部为大写
        # print(spam.islower())       #islower()方法判断字符串是否全部为小写
        # spam='HELLO'
        # print(spam.isupper())
        # print(spam.islower())
        # spam='hello'
        # print(spam.isupper())
        # print(spam.islower())

        # spam='!!!'                  #！不参与判断
        # print(spam.isupper())
        # print(spam.islower())
        # spam='a!!!'                  
        # print(spam.isupper())
        # print(spam.islower())

        # spam='Hello World!'
        # print(spam.upper().isupper())
        # print(spam.lower().islower())

    #isX()字符串方法    
    #isalpha()      如果字符串只包含字母且非空返回True，否则返回False
    #isalnum()      如果字符串只包含字母和数字且非空返回True，否则返回False
    #isdecimal()    如果字符串只包含数字字符且非空返回True，否则返回False
    #isspace()      如果字符串只包含空格、制表符和换行且非空返回True，否则返回False
    #istitle()      如果字符串仅包含以大写字母开头、后面都是小写字母的单词返回True，否则返回False

        # spam='asdwSwd'              #isalpha()方法验证
        # print(spam.isalpha())
        # spam='asdwSwd123'
        # print(spam.isalpha())

        # spam='asdwSwd123'           #isalnum()方法验证s
        # print(spam.isalnum())
        # spam='asdwSwd'
        # print(spam.isalpha())
        # spam='asdwSwd123!!!1'
        # print(spam.isalpha())

        # spam='asdwSwd123!!!'       #isdecimal()方法验证
        # print(spam.isdecimal())
        # spam='1230'
        # print(spam.isdecimal())
        # spam='123!'
        # print(spam.isdecimal())

        # spam='123'                 #isspace()方法验证
        # print(spam.isspace())
        # spam='   '
        # print(spam.isspace())
        # spam='\t  \t  \t  \n\n '
        # print(spam.isspace())

        # spam='Hello 123'           #istitle()方法验证
        # print(spam.istitle())
        # spam='Hello !\n'
        # print(spam.istitle())
        # spam='hello !\n'
        # print(spam.istitle())
        # spam='Hellow World'
        # print(spam.istitle())
        # spam='Hellow aaa World'
        # print(spam.istitle())

        # while True:
        #     print('输入你的年龄')
        #     age=input()
        #     if age.isdecimal():
        #         break
        #     else:
        #         print('只能输入数字')
        # while True:
        #     print('输入你的密码')
        #     password=input()
        #     if password.isalnum():
        #         break
        #     else:
        #         print('只能输入数字和字母')

    #字符串方法startswith()和endswith()
        # spam='Hello World!'
        # print(spam.startswith('Hello'))
        # print(spam.endswith('World!'))
        # spam='abcd123'
        # print(spam.startswith('abcddd'))
        # print(spam.endswith('12'))
        # spam='Hello World!'
        # print(spam.startswith('Hello World!'))
        # print(spam.endswith('Hello World!'))

    #字符串方法 join() 和 split()
        # spam=['cat','rats','bats']      #join()方法可以将字符串列表连接起来
        # symbol='|'
        # print(symbol.join(spam))
        # symbol=' '
        # print(symbol.join(spam))
        # symbol=','
        # print(symbol.join(spam))
        #
        # reNew='\n'.join(spam)            #这种方法更为简便
        # print(reNew)
        #
        # reNew='-'.join(spam)
        # print(reNew)

        # spam='aaa bbb ccc eee ddd iii'
        # print(spam.split())
        # spam='1a2a3a4a5a6'
        # print(spam.split('a'))
        # spam='''你好阿
        # 我不好
        # 为什么
        # 吵架了
        # 为什么吵架
        # 因为我的女朋友'''
        # print(spam.split('\n'))

    #使用partition()方法分隔字符串  将字符串以指定分隔符分割成三部分
        # spam='Hello World!'
        # print(spam.partition('World'))
        # print(spam.partition('W'))
        # print(spam.partition(' '))
        # print(spam.partition('YXZ'))
        # spam='o1o2o3o4o5'
        # print(spam.partition('o'))
        # spam='Hello World!'
        # a,b,c=spam.partition(' ')
        # print(a,b,c)

    #使用rjust()、ljust()和center()方法对齐字符串
    # rjust方法会在字符串右边填充空格，ljust方法会在字符串左边填充空格 会将字符串本身的长度计算进去
        # spam='Hello World!'
        # print(spam.rjust(20))   #rjust()方法会从字符串右边开始填充 默认填充空格
        # print(spam.rjust(13))

        # print(spam.ljust(20))   #ljust()方法会从字符串左边开始填充 默认填充空格
        # print(spam.ljust(13))

        # print(spam.rjust(20,'-'))   #rjust和ljust方法可以指定填充字符
        # print(spam.rjust(13,'-'))
        # print(spam.ljust(20,'-'))
        # print(spam.ljust(13,'-'))

        # print(spam.center(20,'='))  #center()方法会在字符串两边填充字符

        # def printPicnic(itmesDict,leftWidth,rightWidth):
        #     print('露营项目'.center(leftWidth+rightWidth,'-'))
        #     for k,v in itmesDict.items():
        #         print(k.ljust(leftWidth,'-') + str(v).rjust(rightWidth))

        # picnicItems={'sandwiches':4,'apples':12,'cpus':4}
        # printPicnic(picnicItems,12,5)
        # printPicnic(picnicItems,20,6)

    #用strip()、rstrip()和lstrip()方法删除空白字符
        # spam='     Hello World!     '
        # print(spam)
        # print(spam.strip())
        # print(spam.lstrip())
        # print(spam.rstrip())
        # spam='aacHelow aacWorld!aacaa'
        # print(spam.strip('aac'))

#使用ord()和chr()函数的字符的数值   将字符转换成Unicode代码点 将Unicode代码点转换成字符
    # print(ord('A'))
    # print(ord('4'))
    # print(ord('!'))
    # print(ord('你'))
    # print(chr(65))

    # print(chr(ord('A')+1))
    # print(chr(ord('A')-1))

    # print(ord('A')<ord('B'))
    # print(ord('A')>ord('B'))

#用pyperclip模块复制和粘贴字符串
    # import pyperclip
    # pyperclip.copy('这是一个使用pyperclip模块的测试，将会在你的剪切板中显示！！！')
    # print(pyperclip.paste())

#字符串格式化
    # num=1
    # formatted=f"{num:02d}"    #0是填充符 2是指定长度 d是整数字符
    # print(formatted)