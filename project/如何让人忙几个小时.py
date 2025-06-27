'''这个程序的主要作用是一个循环，
    比如：问题是1 你回答yes或者no 回答yes 重复问题1 no则结束
'''
import pyinputplus as pyip

prompt = '你知道怎么让人忙碌几个小时吗？'
response = pyip.inputYesNo(prompt)
while True:
    if response=='yes':
        response = pyip.inputYesNo(prompt)
    else:
        print('谢谢的你的回答')
        break