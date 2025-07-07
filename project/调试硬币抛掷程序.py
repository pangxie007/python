import random,logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable()

guess = input('猜两次硬币，输入是正还是反！！ 0=正 1=反\n')
toss=random.randint(0,1)
logging.debug(f'toss={toss} guess={guess}')

if toss==int(guess):
    print('你得到了一枚硬币,开始第二轮！！')
    toss = random.randint(0, 1)
    guess=input('0=正 1=反\n')
    logging.debug(f'toss={toss} guess={guess}')
    if toss == int(guess):
        print('两轮你都赢了！！！')
    else:
        print('只猜中了一次，很遗憾~')
else:
    print('没有猜对 继续猜！')
    toss = random.randint(0, 1)
    guess=input('0=正 1=反\n')
    logging.debug(f'toss={toss} guess={guess}')
    if toss == int(guess):
        print('你得到了一枚硬币,但是很遗憾你只赢了一轮')
    else:
        print('真倒霉，两次都没猜中')
