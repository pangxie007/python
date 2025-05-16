#由于平板原因 不能进行ctrl+c操作所以这里没有定义try和except
import time,sys
indent = 0
indentIncreasing = True
while True:
    print(' ' * indent, end='')
    print('***********')
    if indentIncreasing:
        indent += 1
        time.sleep(0.1)
        if indent == 20:
            indentIncreasing = False
    else:
        indent -= 1
        time.sleep(0.1)
        if indent == 0:
            indentIncreasing = True
sys.exit()