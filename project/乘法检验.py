import pyinputplus as pyip
import random,time
numberOfQuestions=10
correctAnswers=0
for questionNumber in range(numberOfQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    prompt='#%s: %s X %s = ' %(questionNumber,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)]
                            ,blockRegexes=[('.*','Incorrect!')]
                            ,timeout=8,limit=3)
    except pyip.TimeoutException:
        print("输入超时")
    except pyip.RetryLimitException:
        print("多次验证失败！！！")
    else:
        print('correct')
        correctAnswers+=1
        time.sleep(1)
print(f'成绩显示:{correctAnswers}/{numberOfQuestions}')