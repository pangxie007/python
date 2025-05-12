# if else elif 语句
name='Bob'
if name == 'Alice':
    print('Hi,Alice')
elif name == 'Bob':
    print('Your name is Bob')
else:
    print('name no valide')

# while 循环
spam = 0
while spam < 5:
    print('Hello world')
    spam+=1

# name = ''
# while name != 'your name':
#     print('Please input your name')
#     name = input()
# print('Thank you')

# break 语句
# name = ''
# while name != 'px':
    # print('please input your name.')
    # name = input()
    # if name == 'px':
        # break
# print('Thank you')

# continue 语句
# while True:
    # print('Who are you?')
    # name = input()
    # if name != 'px':
        # continue
    # print('Hello px. What is the password?')
    # password = input()
    # if password == '123456':
        # break
# print('Access granted')

# for 循环和 range（）函数
print('My name is')
for i in range(5):
    print('My name is px (' + str(i) + ')')
    if str(i) == '3':
        break

total=0
for num in range(101):
    total+=num
print(total)

print('My name is')
i =0
while i<5:
    print('My name is px (' + str(i) + ')')
    i+=1

# range（）函数
for i in range(12,16):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(5,-1,-1):
    print(i)