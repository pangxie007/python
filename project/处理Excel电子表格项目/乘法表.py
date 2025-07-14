import sys,logging,openpyxl,pyinputplus
#日志管理区
# logging.disable()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug(f'接收到了{sys.argv}个参数')


#excel文件管理区
wb=openpyxl.load_workbook(r'D:\python\project\project\处理Excel电子表格项目\outdata.xlsx')
sheet=wb.active
#获取文件大小
    #input方式获取
    # n=pyinputplus.inputInt('输入乘法表大小:')
#sys.argv方式获取
if len(sys.argv)==2:
    n=sys.argv[1]

#生成乘法表
for a in range(int(n)):
    for b in range(int(n)):
        if a > b:
            continue
        out=a*b
        # print(f'{a}*{b}={out}')
        # sheet.cell(row=a+1,column=b+1).value=f'{a}*{b}={out}'
        sheet.cell(row=b + 1, column=a + 1).value = f'{a}*{b}={out}'

print('乘法表生成完毕！')
wb.save(r'D:\python\project\project\处理Excel电子表格项目\outdata.xlsx')
wb.close()