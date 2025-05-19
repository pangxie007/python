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
    # spam=[222,234,12,24,21,556,3,-21,-2,0]
    # spam.sort()
    # print(spam)

    # spam=['z','Z','a','aa','aaa','AA']  
    # spam.sort()
    # print(spam)

    # spam=['z','Z','a','aa','aaa','AA'] 
    # spam.sort(key=str.lower)
    # print(spam)

    # spam=[4,3,2,1,'a','b']
    # try:
    #   spam.sort()
    # except TypeError:
    #   print('列表中存在不同类型的数据')

  #使用 reverse() 方法对列表进行反向排序
    # spam=[1,2,3,4,5]
    # spam.reverse()
    # print(spam)

  #python中缩进规则的例外
    # spam=[1,

    # 2,        31,

    #       4]
    # print(spam)

  #例子程序，神奇8球和列表
    # import random
    # messages=['你今天很幸运',
    # '你今天不太幸运',
    #       '你今天运气一般',
    #     '你今天运气很差',
    #   '你今天运气极差']
    # print(messages[random.randint(0,len(messages)-1)])

#序列数据类型
  # name='Zophie'
  # print(name[0])
  # print(name[-2])
  # print(name[0:4])
  # print(name)
  # print('Z' in name)
  # print('ph' in name)
  # print('op' not in name)
  # for i in name:
    # print(f'*****{i}*****')
  
  #可变和不可变数据类型 列表属于可变数据类型 字符串属于不可变数据类型
    # name='Zophie'
    # nameList=[1,2,3,4]
    # try:
    #   name[0]='2'
    # except TypeError:
    #   print('字符串数据类型是不可变数据类型')
    # nameList[0]=2
    # print(nameList)

  #元组数据类型
    # eggs=('hello',42,0.5)
    # spam=[1,2,3,4,0.5]
    # print(type(eggs))
    # print(type(spam))
    # print(eggs)
    # print(spam)
    # print(eggs[0])
    # print(eggs[1:3])
    # print(len(eggs))

    # try:
    #   eggs[0]=1
    # except TypeError:
    #   print('元组数据类型是不可变数据类型')

    # spam=(1,2,3,4,4)
    # print(type(('hello')))
    # print(type(('hello',)))
    # print(type((9)))
    # print(type((1,0)))
    # print(type(spam))

  #用list（）和 tuple（）函数来转换数据类型
    # spam=['hello',1,2]
    # spamTuple=('hh',2,2,2)
    # print(type(spam))
    # print(type(tuple(spam)))
    # print(spam)

    # print(type(spamTuple))
    # print(type(list(spamTuple)))
    # print(spamTuple)

#引用
  # spam=42
  # cheese=spam
  # spam=100
  # print(spam)
  # print(cheese)

  # spam=[0,1,2,33]
  # cheese=spam
  # cheese[1]=100
  # print(spam)
  # print(cheese)

  #标识和id（）函数
    # print(id('aaaa'))
    # spam='aaaa'
    # print(id(spam))
    # spam+='bbb'
    # print(id(spam))

    # spam=[1,1,2,2]
    # print(id(spam))
    # spam+=[3,3]
    # print(id(spam))
    # spam.append(4)
    # print(id(spam))
    # print(spam)

  #传递引用
    # def eggs(someParameteer):
    #   someParameteer.append('Hello')
    # spam=[1,1,2,2]
    # eggs(spam)
    # print(spam)

  #copy模块的 copy()和deepcopy()函数 copy函数只会复制第一层列表【字列表的id相同】 deepcopy函数会复制所有列表
    # import copy
    # spam=[1,2,3,[4,5,6]]
    # print('spam主列表ID:',end=' ')
    # print(id(spam))
    # print('spam子列表ID:',end=' ')
    # print(id(spam[3][:]))
    # print('spam字列表元素ID:',end=' ')
    # print(id(spam[3][0]))

    # aaaa=copy.deepcopy(spam)
    # print('aaaa主列表ID:',end=' ')
    # print(id(aaaa))
    # print('aaaa子列表ID:',end=' ')
    # print(id(aaaa[3][:]))
    # print('aaaa子列表元素ID:',end=' ')
    # print(id(aaaa[3][0]))

    # print('copy')
    # spam=[1,2,3,[4,5,6]]
    # print('spam追了表ID:',end=' ')
    # print(id(spam))
    # print('spam子列表ID:',end=' ')
    # print(id(spam[3][:]))
    # print('spam子列表元素ID:',end=' ')
    # print(id(spam[3][0]))

    # bbbb=copy.copy(spam)
    # print('bbbb主列表ID:',end= ' ')
    # print(id(bbbb))
    # print('bbbb子列表ID:',end= ' ')
    # print(id(bbbb[3][:]))
    # print('bbbb子列表元素ID:',end= ' ')
    # print(id(bbbb[3][0]))