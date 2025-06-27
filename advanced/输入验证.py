#pyinputplus模块
# import pyinputplus as pyip
# a=pyip.inputNum(prompt='请输入你要指定的数值：')
# print(a)

#关键字参数min max greaterThan lessThan
# import pyinputplus as pyip
# response=pyip.inputNum('输入数值:',min=4)
# print(response)
# response=pyip.inputNum('输入数值:',greaterThan=4)
# print(response)
# response=pyip.inputNum('>',min=4, lessThan=6)
# print(response)

#关键字参数blank
# import pyinputplus as pyip
# response=pyip.inputNum('输入数值:',blank=True)
# print(response)

#关键字参数limit timeout default
# import pyinputplus as pyip
# response=pyip.inputNum('输入数值:',limit=2)
# print(response)
# response=pyip.inputNum('输入数值:',timeout=10)
# print(response)
# response=pyip.inputNum(limit=2,default='N/A')
# print(response)

#关键字参数allowRegexes blockRegexes
# import pyinputplus as pyip
# response=pyip.inputNum(allowRegexes=(r'(I|V|X|L|C|D|M)+',r'zero'))
# print(response)
# response=pyip.inputNum(allowRegexes=(r'(i|v|x|l|c|d|m)+',r'zero'))
# print(response)
# response=pyip.inputNum(blockRegexes=[r'[02468]$'])
# print(response)

#将自定义验证函数传递给inputCustom()
# import pyinputplus as pyip
# def addsUpToTen(numbers):
#     numberList = list(numbers)
#     for i,digit in enumerate(numbers):
#         numberList[i]=int(digit)
#     if sum(numberList)!=10:
#         raise Exception(f'数字综合必须等于10，而不是{sum(numberList)}')
#     return int(numbers)
#
# response=pyip.inputCustom(addsUpToTen)
# print(response)