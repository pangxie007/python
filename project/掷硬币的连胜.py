import random,copy,time

coin_all=[]
coin=[]

for i in range(10000):
    if random.randint(0,1)==1:
        coin.append('H')
    else:
        coin.append('T')

coin_all=copy.copy(coin)

#每次一次投掷硬币的随机表 下面检查代码统计这个列表来计算出概率
# print(coin_all)
# print()

#检查连胜
accomplish_H=0
accomplish_T=0
amount_H=0
amount_T=0
for i in range(len(coin_all)-1): #如果不 -1 下面if中的[i+1]循环到最后一个索引100时会操出列表索引范围
    if coin_all[i]=='H' and coin_all[i+1]=='H':
        amount_H +=1
    elif coin_all[i]=='T' and coin_all[i+1]=='T':
        amount_T +=1
    else:
        amount_H =0
        amount_T =0

    if amount_H == 5: #如果设置的是= 那么 超出之后也不算
        accomplish_H +=1
        amount_H=0
    elif amount_T == 5:
        accomplish_T +=1
        amount_T=0

print('连续出现6次H的次数为:'+ str(accomplish_H))
print('连续出现6次T的次数为:'+ str(accomplish_T))
print('在这个10000次随机掷硬币的情况下，连续6次都是正面的概率是：' + str(accomplish_H/10000) + '，连续6次都是反面的概率是：' + str(accomplish_T/10000))