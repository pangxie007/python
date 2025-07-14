import sys,openpyxl

#设置excel基础信息
wb=openpyxl.load_workbook(rf"D:\python\project\project\处理Excel电子表格项目\{sys.argv[3]}")
sheet=wb.active

if len(sys.argv) == 4:
    sheet.insert_rows(int(sys.argv[1]),int(sys.argv[2]))
else:
    print('输入参数错误')

print('插入完成')
wb.save(rf"D:\python\project\project\处理Excel电子表格项目\{sys.argv[3]}")