theBroad={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking','5c':'bbishop','0a':'wqueen'}
qipang={}
def checkBroad(Broad):
    global qipang
    elemental={'wking':1,'bking':1,'wqueen':1,'bqueen':1,'wbishop':2,'bbishop':2,'wrook':2,'brook':2,'wnight':2,'bnight':2,'wpawn':8,'bpawn':8}
    broadAmount={}
    for x in range(8,-1,-1):
        for y in 'abcdefgh':
            qipang.setdefault(str(x)+y,' ')
    for k,v in theBroad.items():
        amount=0
        if k not in qipang.keys(): #判断地址是否溢出
            print(f'地址{k}:{v}溢出')
            return False
        for v1 in theBroad.values(): #计算棋子数量
            if v == v1:
                amount+=1
        broadAmount[v]=amount
    print(broadAmount)
    for k,v in broadAmount.items():
        if elemental[k]<v:
            print(f'棋子{k}数量超出限制')
            return False
checkBroad(0)


a=0
for i in qipang:
    a+=1
    print(i,end=' ')
    if a==8:
        print()
        a=0
