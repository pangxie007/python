TableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'], 
           ['dogs','cats','moose','goose']]

def printTable(data): 
    #轮询二维列表 将二位列表中的元素长度存储在TBlen列表中 使用sort方法排列获取最大值
    TBlen=[]
    for y in range(len(data)):
        for x in range(len(data[0])):
            # print(data[y][x],end=' ')
            TBlen.append(len(data[y][x]))
    TBlen.sort()
    print(TBlen)
    
    #获取最大值 进行左对齐
    maxlen=TBlen[-1]
    for y in range(len(data)):
        print()
        for x in range(len(data[0])):
            print(data[y][x].ljust(maxlen),end=' ')

printTable(TableData)