#读取Excel文档
    # import openpyxl
    # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx')
    # print(type(wb))
    #
    # #从工作簿中获取工作表
    # print(wb.sheetnames)
    #
    # #获取当前表名 title
    # sheet=wb['example']
    # print(sheet)
    # print(type(sheet))
    # print(sheet.title)
    #
    # #获取当前活动工作表 active
    # anotherSheet=wb.active
    # print(anotherSheet)

#从表中取得单元格
    # import openpyxl
    # wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx")
    #查看 excel 中有多少子表
    # print(wb.sheetnames)
    #
    # #获取 A1 单元格信息
    # sheet=wb['example']
    # print(sheet)
    # print(sheet['A1'])
    # print(sheet['A1'].value)
    #
    # #获取 B1 单元格信息
    # c=sheet['B1']
    # print(c)
    # print(c.value)
    # print(f"行:{c.row} 列:{c.column} 值:{c.value}")
    # print(f"坐标:{c.coordinate} 值:{c.value}")
    #
    # #获取 C1 单元格值
    # print(sheet['C1'].value)
    #
    # #用 cell 方法获取值
    # print(sheet.cell(row=1,column=2))
    # print(sheet.cell(row=1,column=2).value)
    # for i in range(1,4):
    #     print(i,sheet.cell(row=i,column=2).value)

#确定表的大小
    # import openpyxl
    # wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx")
    # sheet=wb['example']
    # print(sheet.max_row)
    # print(sheet.max_column)

#列字母和数字之间的转换
    # import openpyxl
    # from openpyxl.utils import get_column_letter,column_index_from_string
    # print(get_column_letter(1))
    # print(get_column_letter(2))
    # print(get_column_letter(27))
    # print(type(get_column_letter(1)))
    #
    # wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx")
    # sheet=wb['example']
    # print(get_column_letter(sheet.max_column))
    #
    # print(column_index_from_string('A'))
    # print(column_index_from_string('AA'))

#从表中取得行和列
# import openpyxl
# wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx")
# sheet=wb['example']
# print(tuple(sheet['A1':'C4']))
# for rowOfCellobjects in sheet['A1':'C4']:
#     for cellobjects in rowOfCellobjects:
#         print(cellobjects.coordinate,cellobjects.value)
#     print('第一行结束')

    #访问特定的列
    # import openpyxl
    # wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_2.xlsx")
    # sheet=wb.active
    # print(list(sheet.columns)[1])
    # for x in list(sheet.columns)[1]:
    #     print(x.value)

#从电子表格中取得数据
    # import openpyxl,pprint
    #
    # wb=openpyxl.load_workbook(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\censuspopdata.xlsx")
    # sheet=wb.active
    # CountryData={}
    # for row in range(2,sheet.max_row+1):
    #     state=sheet['B'+str(row)].value
    #     country=sheet['C'+str(row)].value
    #     pop=sheet['D'+str(row)].value
    #
    #     CountryData.setdefault(state,{})
    #     CountryData[state].setdefault(country,{'tracts':0,'pop':0})
    #     CountryData[state][country]['tracts']+=1
    #     CountryData[state][country]['pop']+=int(pop)
    # print(CountryData['AL'])
    # resultFile=open(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\census2010.py','w')
    # resultFile.write('allData = ' +pprint.pformat(CountryData))
    # resultFile.close()

    #读取处理完成的内容
    # import os
    # from FunctionTest.处理Excel电子表格测试目录 import census2010
    # print(census2010.allData['AK']['Anchorage'])
    # print(census2010.allData['AK']['Anchorage']['pop'])

    #从表中取得公式的结果 而不是公式
"""
当使用 data_only=True 时返回 None，通常是因为 Excel 文件未在 Excel 中 实际计算并保存过结果（openpyxl 的 data_only 依赖 Excel 保存的缓存计算值，而非实时计算）。
如果这个excel文件是python语言创建的 那么需要打开文件之后使用保存 才可以访问到文件内容
"""
    # import openpyxl
    # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\公式.xlsx',data_only=True)
    # sheet=wb.active
    # print(sheet['A3'].value)

#写入Excel文档
    #创建并保存excel文档
        # import openpyxl
        # wb=openpyxl.Workbook()
        # print(wb.sheetnames)
        # sheet=wb.active
        # print(sheet)
        # print(sheet.title)
        # sheet.title='newExcel'
        # print(sheet.title)
        # print(wb.sheetnames)

        # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\example.xlsx')
        # sheet=wb.active
        # sheet.title='NewSheet'
        # wb.save('D:\python\project\FunctionTest\处理Excel电子表格测试目录\example_copy.xlsx')

    #创建和删除工作表
        # import openpyxl
        # wb=openpyxl.Workbook()
        # print(wb.sheetnames)
        # wb.create_sheet()
        # print(wb.sheetnames)
        # wb.create_sheet(index=0,title='First Sheet')
        # print(wb.sheetnames)
        # wb.create_sheet(index=2,title='Two Sheet')
        # print(wb.sheetnames)
        # del wb['Sheet']
        # print(wb.sheetnames)
        # del wb['Sheet1']
        # print(wb.sheetnames)
        # wb.save('D:\python\project\FunctionTest\处理Excel电子表格测试目录\createORdell.xlsx')

    #将值写入单元格
        # import openpyxl
        # wb=openpyxl.Workbook()
        # sheet=wb['Sheet']
        # print(sheet['A1'].value)
        # sheet['A1']='Hello,World!'
        # print(sheet['A1'].value)

    #插入行.xlsx
        # import openpyxl
        # wb=openpyxl.Workbook()
        # print(type(wb))
        # sheet=wb.active
        #
        # sheet['A1']='Hello World!'
        # sheet.insert_rows(1,1)
        #
        # wb.save(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\插入行.xlsx")

#项目：更新电子表格
    # import openpyxl
    # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\produceSales.xlsx')
    # sheet=wb.active
    #第一版
        # #需要更改的定价
        # New_Garlic=1.19
        # New_Celery=3.07
        # New_Lemon=1.27
        #
        # #遍历excel表格 找到对应的蔬菜价格
        # for row in range(2,sheet.max_row+1):
        #     produce=sheet['A'+str(row)].value
        #     cost_pre_pound=sheet['B'+str(row)].value
        #     #判断是否是需要修改的蔬菜
        #     if produce=='Lemon':
        #         #修改蔬菜价格
        #         sheet['B'+str(row)]=New_Lemon
        #     elif produce == 'Garlic':
        #         #修改蔬菜价格
        #         sheet['B'+str(row)]=New_Garlic
        #     elif produce == 'Celery':
        #         #修改蔬菜价格
        #         sheet['B'+str(row)]=New_Celery

    #第二版 使用字典
    # PRICE_UPDATES={'Gralic':1.19,
    #                'Celery':3.07,
    #                'Lemon':1.27}
    # for i in range(2,sheet.max_row+1):
    #     produce=sheet.cell(row=i,column=1).value
    #     if produce in PRICE_UPDATES:
    #         sheet.cell(row=i,column=2).value=PRICE_UPDATES[produce]

    #保存修改后的excel
    # wb.save(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\aaa.xlsx")
    # print('单价修改完毕')

#设置单元格的字体风格
    # import openpyxl
    # from openpyxl.styles import Font
    # wb=openpyxl.Workbook()
    # sheet=wb['Sheet']
    # italic24Font=Font(size=24,italic=True)
    # sheet['A1'].font=italic24Font
    # sheet['A1']='Hello World!'
    # wb.save(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\wordStyles.xlsx")

#Font对象
    # import openpyxl
    # from openpyxl.styles.fonts import Font
    # wb=openpyxl.Workbook()
    # sheet=wb['Sheet']
    #
    # fontobj1=Font(name='Times New Roman',bold=True)
    # sheet['A1'].font=fontobj1
    # sheet['A1']='Bold Times New Roman'
    #
    # fontobj2=Font(size=24,italic=True)
    # sheet['B3'].font=fontobj2
    # sheet['B3']='24 pt Italic'
    #
    # wb.save(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\Font对象.xlsx')

#公式
    # import openpyxl
    # wb=openpyxl.Workbook()
    # sheet=wb['Sheet']
    #
    # sheet['A1']=100
    # sheet['A2']=200
    # sheet['A3']='=sum(A1:A2)'
    #
    # wb.save(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\公式.xlsx")

#调整行和列
    #设置行高和列宽
        # import openpyxl
        # wb=openpyxl.Workbook()
        # sheet=wb["Sheet"]
        # sheet['A1']='Tall row'
        # sheet['B2']='Wide column'
        #
        # sheet.row_dimensions[1].height=70
        # sheet.column_dimensions['B'].width=20
        #
        # wb.save(r"D:\python\project\FunctionTest\处理Excel电子表格测试目录\设置行高和列宽.xlsx")

#合并和拆分单元格
    # import openpyxl
    # wb=openpyxl.Workbook()
    # sheet=wb['Sheet']

    #合并
    # sheet.merge_cells('A1:D3')
    # sheet['A1']='Twelve cells merged together.'
    #
    # sheet.merge_cells('C5:D5')
    # sheet['C5']='Two merged cells.'
    # print('合并完毕')

    #拆分
    # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\合并和拆分单元格.xlsx')
    # sheet=wb['Sheet']
    #
    # sheet.unmerge_cells('A1:D3')
    # sheet.unmerge_cells('C5:D5')
    # print('拆分完毕')

    # wb.save(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\合并和拆分单元格.xlsx')

#冻结窗格
    # import openpyxl
    # wb=openpyxl.load_workbook(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\produceSales.xlsx')
    # sheet=wb.active
    #
    # #冻结
    # sheet.freeze_panes='A2'
    # #解冻
    # sheet.freeze_panes=None
    #
    # wb.save(r'D:\python\project\FunctionTest\处理Excel电子表格测试目录\produceSales.xlsx')

#图表 【略】