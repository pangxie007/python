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
    # spam = ['cat','bat','rat','elephant']
    # del spam[2]
    # print(spam)
    # del spam[0]
    # print(spam)

  #使用列表 
    # catName= []
    # while True:
    #   print('给猫猫取名字,现在有' + str(len(catName)) + '猫猫有名字,什么都不输入视为输入结束')
    #   name = input()
    #   if name == '':
    #     break
    #   catName += [name]
    # print(f'猫猫的名字是: ')
    # for name in catName:
    #   print('' + name)
  
  #列表用于循环
    # for i in range(4):
    #   print(i)
    # for i in [0,1,2,3]:
    #   print(i)
    # for i in range(len([0,1,2,3])):
    #   print(i)  
  
  #in 和 not in 操作符
    # a='aaa' in ['a','aa','aaa']
    # s=['a','aa','aaa']
    # print(a)
    # print('aaa' in ['a','aa','aaa'])
    # print('a' in s)
    # print('b' in s)
    # print('b' not in s)

    # mypets= ['Zophie','Pooka','Fat-tail']
    # print('输入一个宠物名字')
    # name = input()
    # if name not in mypets:
    #   print('你输入的宠物名字不在列表中')
    # else:
    #   print('你输入的宠物名字在列表中')

  #多重赋值技巧
    # cat = ['a','aa','aaa']
    # size,name,age=cat
    # print(size,name,age)

    # try:
    #   size,name,age,error=cat
    #   print(size,name,age,error)
    # except ValueError:
    #   print('列表长度与变量数量不匹配')
  
  #enumerate()函数与列表一起使用 enumerate()函数会返回一个int类型的索引和索引对应的值，enumerate(somelist,start=0)可以指定索引的起始值
    # aaa=['a','aa','aaa']
    # for index,item in enumerate(aaa):
    #   print('Index is '+ str(index) +' value is ' + item)
    #   print(f'Index is {index} value is {item}')

  #random.choice 和 random.shuffle函数与列表一起使用 random.choice从列表中随机选择一个元素 random.shuffle将列表中的元素随机排序
    # import random
    # aaa=['a','aa','aaa']
    # print(random.choice(aaa))
    # random.shuffle(aaa)
    # print(aaa)

  #增强的赋值操作 += -= *= /= %= 
    # a=1
    # a+=1
    # print(a)
    # a-=1
    # print(a)
    # a*=2
    # print(a)
    # a/=2
    # print(a)
    # a%=2
    # print(a)

#方法
# spam=['a','aa','aaa','aa']
# print(spam.index('a'))
# print(spam.index('aaa'))
# print(spam.index('aa')) #列表中存在多个重复的 aa 但是只会输出第一个值的索引
# try:
#   print(spam.index('b'))
# except ValueError:
#   print('列表中不存在该元素')

  #用append()方法和 insert()方法在列表中添加元素 append()方法在列表末尾添加元素 insert()方法在列表中插入元素
      # spam=['a','aa','aaa','aa']
      # spam.append('bbb')
      # print(spam)

      # spam.insert(1,'ccc')
      # print(spam)

      # test='aaa'
      # try:
      #   test.append('bbb')
      # except AttributeError:
      #   print('字符串数据类型没有append()方法')

  #用 remove() 方法从列表中删除元素 remove()方法只删除第一个指定的值
    # spam=['a','aa','aaa','aa']
    # spam.remove('aa')
    # print(spam)

    # spam.remove('aaa')
    # print(spam)

    # try:
    #   spam.remove('aaeew')
    # except ValueError:
    #   print('列表中不存在该元素')

  #用 Sort() 方法对列表进行排序
spam=[222,234,12,24,21,556,3,-21,-2,0]
spam.sort()
print(spam)

spam=['a','aa','aaa','aa']  
spam.sort()
print(spam)