import random
import pyinputplus as pyip
tk={
    1:'CAI是()的英文缩写',
    2:'CAI是指()',
    3:'CAM软件可用于计算机()'
    }

xx={
    1:'A:计算机辅助教学	B:计算机辅助设计	C:计算机辅助制造	D:计算机辅助管理',
    2:'A:系统软件	B:计算机辅助教学	C:计算机辅助设计	D:办公自动化系统',
    3:'A:辅助制造	B:辅助测试	C:辅助教学	D:辅助设计'
    }

da={
    1:'A',
    2:'B',
    3:'A'
    }

quizFile=open('ComputerQuizTopic.txt','w',encoding="utf-8")
answerKeyFile=open('ComputerQuizTopic_answer.txt','w',encoding="utf-8")

#对题目进行随机
tk_list=list(tk.keys())
random.shuffle(tk_list)
print(tk_list)

for tm_num in tk_list:

    # # 终端_正常执行语句
    # print(tk[tm_num])
    # print(xx[tm_num])
    # #用户答题机制
    # my_answer=pyip.inputChoice(['A','B','C','D'],'选项:')
    #
    # # 终端_错误判断
    # if my_answer == da[tm_num]:
    #     print("正确")
    # else:
    #     print('错误')

    #将题目和选项合并为一个文件
    quizFile.write(f'{tk[tm_num]}\n{xx[tm_num]}\n')
    answerKeyFile.write(f'{da[tm_num]}\n')

