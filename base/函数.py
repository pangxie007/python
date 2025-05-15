def hello(name):
    print('Hello world' + name)
    print('你好世界' + name)
    print(name)

hello('px')
#return 返回值
    # import random
    # def gitAnswer(answerNumber):
    #     if answerNumber % 2 == 0:
    #         return '偶数'
    #     else:
    #         return '奇数'
    # Number = random.randint(1,10)
    # print(gitAnswer(Number))

#None 值
    # spam = print('aaa')
    # print(type(spam))

    # #关键字参数和print 函数 print的end变元和sep变元
    # print('Hello')
    # print('World')

    # print('Hello',end=' ')
    # print('World')

    # print('px','hdf','pml',sep='-')

#调用栈 【先进后出】
    # def a():
    #     print('a() starts')
    #     b()
    #     d()
    #     print('a() returns')

    # def b():
    #     print('b() starts')
    #     c()
    #     print('b() returns')

    # def c():
    #     print('c() starts')
    #     print('c() returns')

    # def d():
    #     print('d() starts')
    #     print('d() returns')
    # a()

#死循环调用 【理论上已经形成死循环但是python解释器对递归深度设置了显示 默认为1000层 到达1000层时会抛出RecursionError 异常，从而终止递归调用。】
    # def a():
    #     print('a() starts')
    #     b()
    #     print('a() returns')

    # def b():
    #     print('b() starts')
    #     a()
    #     print('b() returns')

    # a()

#局部和全局作用域
    #局部变量不能再全局作用域内使用
    # def spam():
    #     eggs = 31337
    # spam()
    # print(eggs)

    #局部作用域中不能使用其他局部变量
    # def spam():
    #     eggs = 99
    #     bacon()
    #     print(eggs)
    # def bacon():
    #     ham = 101
    #     eggs = 0
    # spam()

    #全局变量可以在局部作用域中读取
    # def spam():
    #     print(eggs)
    # eggs = 42
    # spam()
    # print(eggs)

#名称相同的局部变量和全局变量
    # def spam():
    #     eggs = 'spam local'
    #     print(eggs)
    # def bacon():
    #     eggs = 'bacon local'
    #     print(eggs)
    #     spam()
    #     print(eggs)
    # eggs = 'global'
    # bacon()
    # print(eggs)

#global语句
    # def spam():
    #     global eggs
    #     eggs= 'spam'
    # eggs = 'global'
    # spam()
    # print(eggs)

    #不可以在局部作用域中定义了eggs变量后，又想调用全局变量eggs
    # def spam():
    #     print(eggs)
    #     eggs = 'spam local'
    # eggs = 'global'
    # spam() 
 
#异常处理 【try 和 except 的使用方法】
    # def spam(divideBy):
    #     try:
    #         return 42 / divideBy
    #     except ZeroDivisionError:
    #         print('实参不能为0')
    # print(spam(2))
    # print(spam(12))
    # print(spam(0))
    # print(spam(1))

    #当try捕捉到异常然后将捕捉的异常和except 指定的异常进行对比 符合条件时 执行except中的代码 不符合则不管
    # def spam(divideBy):

    #     return 42 / divideBy
    # try:
    #     print(spam(2))
    #     print(spam(12))
    #     print(spam(0))
    #     print(spam(1))
    # except ZeroDivision:
    #     print('实参不能为0')