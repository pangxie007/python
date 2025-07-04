'''
    这个文件用来测试random模块的方法功能
    random.sample(population, k)
        population：要抽取的总体，可以是列表、元组、字符串或集合。
        k：要抽取的元素个数，必须满足 0 ≤ k ≤ len(population)。
'''
# import random
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sample = random.sample(numbers, 3)  # 随机抽取 3 个不重复的元素
# print(sample)  # 例如：[5, 1, 9]

import random
aaa=['a','aa','aaa']
print(random.choice(aaa))
a={1:'a',2:'b',3:'c'}
random.shuffle(a)
print(a)