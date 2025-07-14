#抛出异常 【raise】
    # raise Exception("这是一个实验性异常")
    # raise TypeError("这是一个实验性异常")

    # def boxPrint(symbol,width,height):
    #     if len(symbol)!=1:
    #         raise Exception("字符未定义")
    #     if width <=2:
    #         raise Exception("宽度必须大于2")
    #     if height <=2:
    #         raise Exception("高度必须大于2")
    #     print(symbol * width)
    #     for i in range(height-2):
    #         print(symbol+(' '*(width-2))+symbol)
    #     print(symbol*width)
    # for sym,w,h in (('*',4,4),('O',20,5),('x',15,3),('Zz',3,3)):
    #     try:
    #         boxPrint(sym,w,h)
    #     except Exception as err:
    #         print(f"有一个例外发生:{err}")

#异常处理
    # try:
    #     # 可能会抛出异常的代码
    #     pass
    # except ExceptionType1:
    #     # 处理特定类型的异常
    #     pass
    # except ExceptionType2:
    #     # 处理另一种类型的异常
    #     pass
    # else:
    #     # 如果没有异常发生，执行此代码块
    #     pass
    # finally:
    #     # 无论是否发生异常，都会执行此代码块
    #     # 通常用于清理资源（如关闭文件、释放锁等）
    #     pass

#取得回溯字符串
    # def spam():
    #     bacon()
    # def bacon():
    #     raise Exception("这个错误是为了取得回溯字符串")
    # spam()

    #将错误日志导出到文件中
    # import traceback
    # try:
    #     raise Exception("这个错误是为了取得回溯字符串")
    # except:
    #         errorFile=open(r"D:\python\project\FunctionTest\调试测试目录\erro_log.txt",'w',encoding='utf_8')
    #         errorFile.write(traceback.format_exc())
    #         errorFile.close()

# 断言
    # ages=[12,23,45,32,13,54,11]
    # ages.sort()
    # print(ages)
    # assert ages[0]<=ages[-1]
    #
    # ages=[11,12,23,45,32,13,54]
    # ages.reverse()
    # print(ages)
    # assert ages[0]<=ages[-1]

#在交通灯模拟中使用断言
#略

#日志
#使用logging模块
    # import logging
    # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
    # logging.debug('开始程序')
    #
    # def factorial(n):
    #     logging.debug('开始 阶乘(%s%%)'% (n))
    #     total=1
    #     for i in range(1,n+1):
    #         total*=i
    #         logging.debug(f'i 是 {str(i)} ,total 是 {str(total)}')
    #     logging.debug('结束 阶乘(%s%%)'% (n))
    #     return total
    #
    # print(factorial(5))
    # logging.debug('结束程序')

#不要用print测试
'''代码理论性来说避免使用print()来进行测试，因为不好删除 以及后期维护量很大'''
from tokenize import endpats

#日志级别
'''
DEBUG   
INFO
WARNING
ERROR
CRITICAL
'''
import logging
    # # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
    # logging.basicConfig(level=logging.ERROR,format='%(asctime)s-%(levelname)s-%(message)s')
    # logging.debug('一些调试细节')
    # logging.info('模块工作日志')
    # logging.warning('关于日志的错误信息')
    # logging.error('发送的错误')
    # logging.critical('程序没有恢复！')

#禁用日志
    # import logging
    # logging.disable()
    # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
    # # logging.disable(logging.CRITICAL)
    # logging.debug('一些调试细节')
    # logging.info('模块工作日志')
    # logging.warning('关于日志的错误信息')
    # # logging.disable(logging.CRITICAL)
    # logging.error('发送的错误')
    # logging.critical('程序没有恢复！')

#将日志记录到文件
    # import logging
    # logging.basicConfig(filename=r"D:\python\project\FunctionTest\调试测试目录\erro_log.txt",level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s',encoding='utf-8')
    # logging.debug('错误日志收集')
