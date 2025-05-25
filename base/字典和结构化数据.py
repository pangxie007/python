#字典数据类型
    # myCat={'size':'fat','color':'gray','disposition':'loud'}
    # number={1:'one',2:'two',3:'three'}
    # key={1:1,2:2,3:3}
    # print(myCat)
    # print(type(myCat))
    # #索引可以是不同的数据类型，对比列表：列表的索引只能是整数类型,通过几个不同的数据类型可以观察到放回值是根据key的原本类型来进行返回
    # print(myCat['size'])
    # print(type(myCat['size']))

    # print(number[2])
    # print(type(number[2]))

    # print(key[3])
    # print(type(key[3]))
    # #这里的报错类型是 KeyError 而不是 typeError
    # print('you love color is:'+ myCat['color'])
    # try:
    #     print('you love number is:'+ key['3']) 
    # except KeyError:
    #     print('字典返回值的数据类型是整形在 + 号前后需要将数据类型统一')

#字典与列表
    #观察列表和字典的关系
        # 列表是有排序的，不同排序的列表是不相等的。 
        # 字典是不需要排序的，只要键值对内容一致，字典就是相等的。
        # spam=[1,2,3,4]
        # bacon=[2,3,4,1]
        # print(spam==bacon)
        # eggs={'name':'px','species':'cat','age':'0'}
        # ham={'species':'cat','name':'px','age':'0'}
        # print(eggs==ham)
        # eggs={'name':'px','species':'cat','age':'0'}
        # ham={'species':'cat','name':'px','aaa':'0'}
        # print(eggs==ham)
        # try:
        #     print(eggs['name':'age'])
        # except TypeError:
        #     print('因为字典是无须的，所以不能使用切片')

        # birthdays={'px':'三月七日','dhf':'四月十一日'}
        # print('输入一个名字（空白则退出）')
        # while True:
        #     name=input()
        #     if name=='':
        #         break
        #     if name in birthdays:
        #         print(birthdays[name]+'这天是:' + name + '的生日')
        #     else:
        #         print('字典没有记录')
        #         bday=input()
        #         birthdays[name]=bday
        #         print('生日字典以更新')
        #         print(birthdays)
    #keys()、values()和items()方法
        # spam={'color':'red','agge':42}
        # for i in spam.keys():
        #     print(i)
        # for i in spam.values():
        #     print(i)
        # for i in spam.items():
        #     print(i)
        #     print(type(i))
        # print()
        # spam.keys()
        # spam.values()
        # spam.items()
        # #items()方法将字典的键值赋予给不同的变量进行打印
        # for k,v in spam.items():
        #     print(k + ' is ' + str(v))

    #检查字典中是否存在键或值 in he not in
        # spam={'color':'red','agge':42}
        # print('color' in spam.keys())
        # print('red' in spam.values())

        # print('color' not in spam.keys())
        # print('red' not in spam.values())

        # print('color' in spam)
        # print('red' in spam)
    
    #get()方法 只是放回值，不会改变字典
        # spam={'color':'red','agge':42}
        # print(spam)
        # print('我的名字是' + spam.get('name','px') + '如果没有则返回px')
        # print(spam)
        # print('我的年龄是' + str(spam.get('agge',22)) + '如果没有则返回22')
    
    #setdefault()方法
        #传统的检测方法，步骤多
        # spam={'color':'red','agge':42}
        # if 'name' not in spam:
        #     spam['name']='px'
        # print(spam)

        # print(spam.setdefault('love','hdf'))
        # print(spam)
        # #建存在于字典中则打印
        # print(spam.setdefault('color','yellow'))
        # #建不存在于字典中则添加
        # print(spam.setdefault('love','hdf'))
        # print(spam)

        # message='It was a bright cold day in April,and the clocks were striking thirteen.'
        # count={}
        # for chacacter in message:
        #     count.setdefault(chacacter,0)
        #     count[chacacter]=count[chacacter]+1
        # print(count)

#美观的输出 pprint模块中的pprint()函数和pformat()函数
    # import pprint
    # message='It was a bright cold day in April,and the clocks were striking thirteen.'
    # count={}
    # for chacacter in message:
    #     count.setdefault(chacacter,0)
    #     count[chacacter]=count[chacacter]+1
    # pprint.pprint(count)

#使用数据结构对真实世界建模
    # theBorad={'T-L':' ','T-M':' ','T-R':' ',
    #           'M-L':' ','M-M':' ','M-R':' ',
    #           'B-L':' ','B-M':' ','B-R':' '}

    # def printBorad(Borad):
    #     print(Borad['T-L'] + '|' + Borad['T-M'] + '|' + Borad['T-R'])
    #     print('-+-+-')
    #     print(Borad['M-L'] + '|' + Borad['M-M'] + '|' + Borad['M-R'])
    #     print('-+-+-')
    #     print(Borad['B-L'] + '|' + Borad['B-M'] + '|' + Borad['B-R'])
    # def gameTurn(Turn):
    #     global turn
    #     if Turn == 'X':
    #         turn='O'
    #     else:
    #         turn='X'
    # def gameOver(Borad):
    #     global game
    #     if Borad['T-L'] == Borad['T-M'] == Borad['T-R'] != ' ':
    #         print('游戏结束'+ Borad['T-L'] + '赢了')
    #         game= False
    #     elif Borad['M-L'] == Borad['M-M'] == Borad['M-R'] != ' ':
    #         print('游戏结束'+ Borad['M-L'] + '赢了')
    #         game= False
    #     elif Borad['B-L'] == Borad['B-M'] == Borad['B-R'] != ' ':
    #         print('游戏结束'+ Borad['B-L'] + '赢了')
    #         game= False
    #     elif Borad['T-L'] == Borad['M-M'] == Borad['B-R'] != ' ':
    #         print('游戏结束'+ Borad['T-L'] + '赢了')
    #         game= False
    #     elif Borad['T-R'] == Borad['M-M'] == Borad['B-L'] != ' ':
    #         print('游戏结束'+ Borad['T-R'] + '赢了')
    #         game= False
    #     elif Borad['T-L'] == Borad['M-L'] == Borad['B-L'] != ' ':
    #         print('游戏结束'+ Borad['T-L'] + '赢了')
    #         game= False
    #     elif Borad['T-M'] == Borad['M-M'] == Borad['B-M'] != ' ':
    #         print('游戏结束'+ Borad['T-M'] + '赢了')
    #         game= False
    #     elif Borad['T-R'] == Borad['M-R'] == Borad['B-R'] != ' ':
    #         print('游戏结束'+ Borad['T-R'] + '赢了')
    #         game= False
    # turn='X'
    # game=True
    # printBorad(theBorad)
    # for i in range(9):
    #     if game==False:
    #         break
    #     print('你现在是' + turn + '输入你要下棋的位置')
    #     move=input()
    #     if move not in theBorad.keys():
    #         print('地址输入错误')
    #         break
    #     theBorad[move]=turn
    #     gameTurn(turn)
    #     printBorad(theBorad)
    #     if i >=3:
    #         gameOver(theBorad)
    #     if ' ' not in theBorad.values():
    #         print('游戏结束，平局！！！')
    #         break

#嵌套的字典和列表
    # allGuests={'px':{'apples':5,'pretzels':12},
            #    'hdf':{'banaler':3,'ham sandwiches':2},
            #    'cat':{'apples':2,'cups':3}}
    # def totalBrought(gusts,time):
        # number=0
        # for k,v in gusts.items():
            # number+=v.get(time,0)
        # return number
    # print('苹果有' + str(totalBrought(allGuests,'apples')))
    # print('三明治有'+ str(totalBrought(allGuests,'ham sandwiches')))
    # print('杯子有'+ str(totalBrought(allGuests,'cups')))
    # print('辣椒有'+ str(totalBrought(allGuests,'lj')))
