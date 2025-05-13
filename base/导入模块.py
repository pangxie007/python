# 调用整个模块
#import random
#for i in range(5):
#    print(random.randint(1,10))

#调用模块中的函数
# from random import randint
# for i in range(5):
    # print(randint(1,100))

#使用sys模块的exit函数来执行退出操作
#对比break sys.exit 前者是跳出循环，后者是退出程序
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')
   
