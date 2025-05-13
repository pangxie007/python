#我们需要写一个石头剪刀布的小程序，并记录输赢、平局次数
#使用random.randint(1,3)来作为石头剪刀布的随机数来进行判断
#使用sys.exit()来退出程序

import random,sys

#前言
print('欢迎来到石头剪刀布')

#输赢、平局计数器
Wins = 0
Losses = 0
Ties = 0

#核心代码
while True:
    randomNuber = random.randint(1,3)
    if randomNuber == 1:
        computerMove = '石头'
    elif randomNuber == 2:
        computerMove = '剪刀'
    else:
        computerMove = '布'

    #输入
    print('输入你的选择：石头、剪刀、布、退出')
    yourMove = input()

    #比较+计数
    if yourMove == computerMove:
        print('平局')
        Ties += 1
    elif yourMove == '石头' and computerMove == '剪刀':
        print('赢了')
        Wins += 1
    elif yourMove == '石头' and computerMove == '布':
        print('输了')
        Losses += 1
    elif yourMove == '剪刀' and computerMove == '石头':
        print('输了')
        Losses += 1
    elif yourMove == '剪刀' and computerMove == '布':
        print('赢了')
        Wins += 1
    elif yourMove == '布' and computerMove == '剪刀':
        print('输了')
        Losses += 1
    elif yourMove == '布' and computerMove == '石头':
        print('赢了')
        Wins += 1
    #结算
    print('%s Wins |%s Losses |%s Ties' % (Wins, Losses, Ties))
    print('---------------------------------------------------')
    #结束
    if yourMove == '退出':
        print('游戏结束')
        sys.exit()