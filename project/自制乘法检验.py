import random,time,re
numberQuestion=10
correctAnswer=0
js=1
for numberAnswer in range(numberQuestion):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    print(f'{js}#{num1}X{num2}=',end='')

    answer=input()
    if int(answer) == (num1*num2):
        correctAnswer+=1
    else:
        print('答案错误')

    js+=1
time.sleep(1)
print(f'{correctAnswer}/{numberQuestion}')
