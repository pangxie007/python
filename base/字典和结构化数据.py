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
spam={'color':'red','agge':42}
for i in spam.keys():
    print(i)
for i in spam.values():
    print(i)
for i in spam.items():
    print(i)
    print(type(i))
print()
spam.keys()
spam.values()
spam.items()
#items()方法将字典的键值赋予给不同的变量进行打印
for k,v in spam.items():
    print(k + ' is ' + str(v))