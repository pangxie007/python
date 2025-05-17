#列表数据类型
# spam = ['cat','bat']
# string = ['rat','elephant']
# aaa=spam+string
# print(['aaa','bbb','ccc'][2] + ',ddd')
# print(type(aaa))
# print(type(aaa[3]))

  #用索引取得列表中的单个值
# spam = ['cat','bat','rat','elephant']
# print(spam[0])
# spam = [['cat','bat','rat'],[10,20,30,40,50]]
# print(spam[0][1])
# print(spam[1][4])

  #负数索引
# spam = ['cat','bat','rat','elephant']
# print(spam[-1])
# print(spam[-3])
# print('The ' + spam[-1] + 'she dont like,she like the' + spam[-2])

  #利用切片取得自子列表
# spam = ['cat','bat','rat','elephant']
# print(spam[0:4])
# print(spam[1:3])
# print(spam[0:-1])
# print(type(spam[1:2]))

# print(spam[:2])
# print(spam[1:])
# print(spam[:])

 #用len()取得列表的长度
# spam = ['cat','bat','rat','elephant']
# print(len(spam))

  #用索引改变列表中的值
# spam = ['cat','bat','rat','elephant']
# print(spam[1])
# spam[1] = 'a'
# print(spam[1])
# spam[-1] = 2000
# print(spam[:])

  #列表连接和列表复制
# spam = ['cat','bat','rat','elephant']
# aaa = [1,2,3,4]
# print(spam + aaa)
# print([1,1,1,1] + ['a','b','c'])
# print(spam + [2,2,2,2])
# print(spam * 3)

  #del语句删除列表元素
spam = ['cat','bat','rat','elephant']
del spam[2]
print(spam)
del spam[0]
print(spam)
