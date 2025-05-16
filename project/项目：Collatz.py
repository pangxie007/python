def collazt(number):
    if number % 2 == 0:
        number = number // 2
        print(f'{number}')
    elif number % 2 == 1: 
        number = 3 * number + 1
        print(f'{number}')
    global importNumber
    importNumber = number
    return number
try:
    print('请输入一个整数：')
    importNumber = int(input())
    while True:
      if (collazt(importNumber)) == 1:
          print('已计算到最小值')
          break
except ValueError:
    print('请输入一个整数!!!')