#我们需要写一个猜数字的小程序，既然是猜数字那么数字就要有随机性以及难度
#随机性和难度控制可以使用random模块的randint函数解决
import random
secretNumber = random.randint(1,20)
print('请输入你猜的数字，范围：1－20')
for guessTaken in range(1,7):
    guess = int(input())

    if guess < secretNumber:
        print("小了")
    elif guess > secretNumber:
        print('大了')
    else:
        break
if guess == secretNumber:
    print('猜对了！！！')
else:
    print('数字是'+ str(secretNumber) +'你太菜了，下一位！！！')