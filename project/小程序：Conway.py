#导入模块
import random,time,copy
#定义宽和高
WIDTH=60
HEIGHT=20
#初始化 列表和细胞
nextCells=[]
for x in range(WIDTH):
    column=[] #创建一个空列表
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') #添加一个活细胞到列表中
        else:
            column.append(' ') #添加一个死细胞到列表中
    nextCells.append(column) #将列表中的细胞添加到nextCells中

while True:
    print('\n\n\n\n')
    currentCells=copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='') #打印细胞
        print() #换行

    for x in range(WIDTH):
        for y in range(HEIGHT):
            #计算活细胞数量
            leftCoord=(x-1)%WIDTH
            rightCoord=(x+1)%WIDTH
            aboveCoord=(y-1)%HEIGHT
            belowCoord=(y+1)%HEIGHT

            numNeighbors=0

            #周边活性细胞检测
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[x][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[leftCoord][y]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][y]=='#':
                numNeighbors+=1
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbors+=1
            if currentCells[x][belowCoord]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbors+=1
            
            #细胞存活规则定制
            if currentCells[x][y]=='#' and (numNeighbors==2 or numNeighbors==3):
                nextCells[x][y]='#'
            elif currentCells[x][y]==' ' and numNeighbors==3:
                nextCells[x][y]='#'
            else:
                nextCells[x][y]=' '
    print('---------------------------------------------------------')
    time.sleep(1)
