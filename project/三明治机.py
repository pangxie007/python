import pyinputplus as pyip
price={'小麦面包':'2','高粱面包':'2','白面包':'1','鸡肉':'3','土耳其烤肉':'5','火腿':'3','豆腐':'2',}
print('价格表：')
for v,k in price.items():
    print(f'{v}——{k}')
print()
mb_type=pyip.inputMenu(['小麦面包','高粱面包','白面包'])
mb_protin=pyip.inputMenu(['鸡肉','土耳其烤肉','火腿','豆腐'])
pl=pyip.inputYesNo('要奶酪吗？')
num=pyip.inputInt('要多少个三明治？',min=1)
sumPrice=(int(price[mb_type])+int(price[mb_protin]))*num
print(f'一共{sumPrice}元')