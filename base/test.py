def a():
    print('a() starts')
    b()
    print('a() returns')

def b():
    print('b() starts')
    a()
    print('b() returns')

a()