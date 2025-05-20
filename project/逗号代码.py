def douhao(spam):
    spam[-1]='and '+spam[-1]
    print(id(spam))
    return str(spam)
list=['a','aa','aaa','bbb']
print(id(list))
print(type(list))
aaa=douhao(list)
print(id(aaa))
print(aaa)
print(type(aaa))