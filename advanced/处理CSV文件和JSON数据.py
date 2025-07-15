#CSV模块
    #reader对象
        # import csv
        # exampleFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\example.csv')
        # exampleReader=csv.reader(exampleFile)
        # exampleData=list(exampleReader)
        #
        # print(exampleData)
        # print(exampleData[0])
        # print(exampleData[0][0])
        # print(exampleData[0][1])
        # print(exampleData[1])

    #在for循环中，从reader对象读取数据
        # import csv
        # exampleFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\example.csv')
        # exampleReader=csv.reader(exampleFile)
        # for row in exampleReader:
        #     print(f'{exampleReader.line_num}-->{row}')

    #writer对象
        # import csv
        # exampleFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\output.csv','w',newline='')
        # #写入数据
        # exampleWriter=csv.writer(exampleFile)
        # exampleWriter.writerow(['spam','eggs','bacon','ham'])
        # exampleWriter.writerow(['Hello,World!','eggs','bacon','ham'])
        # exampleWriter.writerow([1,2,3.141592,4])
        #
        # exampleFile.close()

    #delimiter 和 lineterminator 关键字参数
        # import csv
        # csvFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\delimiter_lineterminator.csv','w',newline='')
        #
        # csvWriter=csv.writer(csvFile,delimiter='\t',lineterminator='\n\n')
        # csvWriter.writerow(['apples','oranges','grapes'])
        # csvWriter.writerow(['eggs','bacon','ham'])
        # csvWriter.writerow(['spam','spam','spam','spam'])
        #
        # csvFile.close()

    #DictReader 和 DictWriter CSV 对象
        # import csv
        # exampleFIle=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\exampleWithHeader.csv')
        # #使用dictreader方法读取csv文件
        # exampleReader=csv.DictReader(exampleFIle)
        # #遍历CSV
        # for row in exampleReader:
        #     print(row['Timestamp'],row['Fruit'],row['Quantity'])

        #当DictReader遇到没有标题的CSV文件时,用fieldname创建自己的标题
            # import csv
            # exampleFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\example.csv')
            # exampleReader=csv.DictReader(exampleFile,['time','name','amount'])
            # for row in exampleReader:
            #     print(row['time'],row['name'],row['amount'])

        #DictWriter对象使用字典创建CSV文件
            # import csv
            # exampleFile=open(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\DicWriter.csv','w',newline='')
            # #定义写入文件，自定义标题
            # exampleWriter=csv.DictWriter(exampleFile,['Name','Pet','Phone'])
            # #将标题写入csv中
            # exampleWriter.writeheader()
            # #以字典心形式写入数据
            # exampleWriter.writerow({'Name':'px','Pet':'cat','Phone':'123'})
            # exampleWriter.writerow({'Name':'hdf','Pet':'dog','Phone':'456'})
            # exampleWriter.writerow({'Pet':'dog','Phone':'456'})
            # exampleWriter.writerow({'Pet':'aaa','Name':'bbb','Phone':'456'})
            # exampleWriter.writerow({'Phone':'123123123','Pet':'bbb'})
            # exampleFile.close()

#项目：从CSV文件中删除标题行
    # import csv,os
    # #路径定义
    # path=os.listdir(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\项目：从CSV文件中删除标题行')
    # #创建new_csv目录容纳已经修改过的文件
    # os.makedirs(r'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\项目：从CSV文件中删除标题行\new_csv',exist_ok=True)
    # #遍历目录文件
    # for i in path:
    #     #判断文件是否以.csv结尾,如果不是则跳出这次循环
    #     if not i.endswith('.csv'):
    #         continue
    #     #提示符
    #     print('开始重写文件...')
    #     #读取csv文件
    #     file=open(rf'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\项目：从CSV文件中删除标题行\{i}')
    #     fileReader=csv.reader(file)
    #     csvData=[]
    #     #过滤第一行
    #     for row in fileReader:
    #         if fileReader.line_num == 1:
    #             continue
    #         csvData.append(row)
    #     file.close()
    #     #写入文件
    #     file=open(rf'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\项目：从CSV文件中删除标题行\{i}','w',newline='')
    #     fileWriter=csv.writer(file)
    #     for row in csvData:
    #         fileWriter.writerow(row)
    #     file.close()
    # #第二个版本
    #     #过滤第一行
    #     # for row in fileReader:
    #     #     if fileReader.line_num == 1:
    #     #         continue
    #     #     #写入文件
    #     #     file=open(rf'D:\python\project\FunctionTest\处理CSV文件和JSON数据测试目录\项目：从CSV文件中删除标题行\new_csv\{i}','a',newline='')
    #     #     fileWriter=csv.writer(file)
    #     #     fileWriter.writerow(row)
    #     #     file.close()
    #     # file.close()

#JSON和API
#Json模块
    #用 loads 函数读取 JSON
        # import json
        # stringOfJsonData='{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
        # jsonDataPythonValue=json.loads(stringOfJsonData)
        # print(jsonDataPythonValue)

    #用 dumps 函数写出 JSON
        # import json
        # pythonValue={'isCat':True,'miceCaught':0,'name':'Zophie'}
        # jsonValue=json.dumps(pythonValue)
        # print(jsonValue)

#项目：取得当前的天气数据【项目在project中】
