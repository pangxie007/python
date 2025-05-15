def hello(name):
    print('Hello world' + name)
    print('你好世界' + name)
    print(name)

hello('px')
#return 返回值
import random
def gitAnswer(answerNumber):
    if answerNumber % 2 == 0:
        return '偶数'
    else:
        return '奇数'
Number = random.randint(1,10)
print(gitAnswer(Number))
#None 值
spam = print('aaa')
print(spam)
#关键字参数和print 函数 print的end变元和sep变元
print('Hello')
print('World')

print('Hello',end=' ')
print('World')

print('px','hdf','pml',sep='-')