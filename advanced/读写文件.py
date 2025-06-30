#pathlib模块在windows 操作系统与 mac、linux操作系统上使用 path 将返回不同的结果
    # from pathlib import Path
    # myFiles=['accounts.py','details.csv','invite.docx']
    # for i in myFiles:
    #     print(Path(r'C\User\AI',i))
#使用/运算符链接路径
    # import sys
    # from pathlib import Path
    # print(Path('hdf')/'px')
    # print(Path('hdf')/Path('px/eggs'))
    # print(Path('hdf')/Path('px','eggs'))

    # homeFolder=r'C:\User\AI'
    # subFolder='spam'
    # print(homeFolder+'\\'+subFolder)
    # print('\\'.join([homeFolder,subFolder]))
    # print(sys.platform)   #sys.platform方法可以打印出运行环境使用的系统 系统名规则在官方文档中

    # homeFolder=Path(r'C:\User\AI')
    # subFolder=Path('spam')
    # print(homeFolder / subFolder)
    # print(str(homeFolder / subFolder))

#当前工作目录
#pathlib模块没有更改当前目录的方法 os模块有，但是有点老旧
    # from pathlib import Path
    # import os
    # print(Path.cwd())
    # os.chdir(r'D:\python\project\base')
    # print(Path.cwd())

#主目录
    # from pathlib import Path
    # print(Path.home())

#绝对路径与相对路径
r''' 绝对路径是一个完整的地址 比如：C:\User\AI\python.py 这被称之为绝对路径
   相对路径则是一个不完整的地址 比如：..\python.py 这里指上一级目录的python.py文件 地址会根据你当前所在位置而改变
   绝对路径与相对路径的区别是 绝对路径不会因为当前目录而改变 '''

#用os.makedirs()创建新文件夹
r'''
    os.makedirs和pathlib.Path.mkdir方法是有去别的，前者可以级联创建，后者不可以
'''
    # import os,pathlib
    # os.makedirs(r'D:\python\project\os测试目录')
    # pathlib.Path.mkdir(r'D:\python\project\pathlib测试目录')
    # pathlib.Path.mkdir(r'D:\python\project\a\aaa')
    # print(pathlib.Path.cwd())

#处理绝对路径和相对路径
    # from pathlib import Path
    # import os
    # print(Path.cwd())
    # print(Path.cwd().is_absolute())
    # print(Path(r'spam/aaa/www').is_absolute())

    # print(os.path.abspath('..'))    #返回相对路径的绝对路径

    # print(os.path.isabs('.'))       #和Path.is_absolute功能一样判断是否是绝对路径和相对路径
    # print(os.path.isabs(r'D:\python\project\advanced\读写文件.py'))
    #
    # print(os.path.relpath(r'C:\User\AI\python3.exe',r'C:\User\AI')) #分离路径？

#取得文件路径的各部分
    # from pathlib import Path
    # import os
    # p=Path(r'C:\User\AI\python3.py')
    # print(p.anchor) #路径锚点
    # print(p.parent) #路径父目录
    # print(p.name)   #路径文件名
    # print(p.stem)   #路径主体
    # print(p.suffix) #路径后缀
    # print(p.drive)  #路径驱动【windows系统独有】
    #
    # textFilePath=r'C:\User\AI\python3.py'
    # print(os.path.basename(textFilePath))   #路径文件名
    # print(os.path.dirname(textFilePath))    #路径父目录
    # print(os.path.split(textFilePath))      #将路径拆分为元组
    # print(os.sep)
    # print(textFilePath.split(os.sep))
    # print(textFilePath.split('\\'))

#查看文件大小和文件内容
    # import os
    # print(os.path.getsize(r'D:\python\project\README.md'))
    # print(os.listdir(r'D:\python\project'))
    #
    # sum_bit=0
    # for i in os.listdir(r'D:\python\project'):
    #     sum_bit+=os.path.getsize(rf'D:\python\project\{i}')
    # print(sum_bit)

#使用通配符模式修改文件列表
    # from pathlib import Path
    # p=Path(r'D:\python\project\FunctionTest\读写模块测试')
    # print(p.glob('*'))      #glob返回一个生成器对象
    # print(list(p.glob('*')))
    # print(list(p.glob('*.png')))

#检查路径的有效性
    # from pathlib import Path
    # import os
    # winDir=Path(r'D:\python\project')
    # notExistsDir=Path(r'D:\python\wwwdwsw')
    # print(winDir.exists())
    # print(winDir.is_file())
    # print(winDir.is_dir())
    # print()
    # print(notExistsDir.exists())
    # print(notExistsDir.is_file())
    # print(notExistsDir.is_dir())
    # print("===================")

    # print(os.path.exists(winDir))
    # print(os.path.isfile(winDir))
    # print(os.path.isdir(winDir))
    # print()
    # print(os.path.exists(notExistsDir))
    # print(os.path.isfile(notExistsDir))
    # print(os.path.isdir(notExistsDir))

#文件读写过程
    # from pathlib import Path
    # p=Path(r'D:\python\project\FunctionTest\读写模块测试\test.txt')
    # print(p.write_text('Hello world!'))
    # print(p.read_text())

#用open函数打开文件
    # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt')

#读取文件内容
'''
python中没有指针这个说法但是 流位置=指针
p.read()是有一个指针的，当使用p.read()之后指针已经指向文件字符串的末尾了【指针并没有被重置】
在指针已经指向字符串末尾且没有重置的情况下使用p.readlines()则会返回空的列表
上面说到p.read()之后指针没有复位 使用p.seek()方法可以将指针复位 下面的p.readlines()方法就可以正常使用了
seek()设置流的位置    移动指针
tell()返回流的位置    指针当前位置
'''
    # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt')
    # a=p.read()
    # print(a)
    # print(type(a))
    # p.seek(0)
    # print(p.readlines())

#写入文件
    # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt','w')
    # print(p.write('Hello everyone'))
    #
    # # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt','r')   #默认是r权限
    # # print(p.write('aaaaa'))
    #
    # p.close()
    # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt','a')
    # print(p.write(' thie is authory A'))
    #
    # p=open(r'D:\python\project\FunctionTest\读写模块测试\test.txt')
    # print(p.read())

#用 shelve 模块保存变量
'''
在 Python 里，shelve和dbm都是和数据持久化存储相关的模块，用于将 Python 对象保存到文件中，方便后续读取使用
shelve 模块
    简介：
        shelve模块提供了一种简单的方式来存储和检索 Python 对象，它类似于一个字典，不同之处在于它会将数据持久化存储到磁盘文件上。
        shelve模块在背后使用了dbm系列模块来实现数据的存储。
    特点
        操作简便：可以像操作字典一样操作 shelve对象，对于熟悉字典操作的 Python 开发者来说很容易上手。
        支持多种对象类型：能够存储几乎所有的 Python 内置对象，比如列表、字典、类实例等 ，不过存储类实例时，类定义需要在运行环境中可访问。
        自动缓存：shelve会在内存中缓存数据，在频繁读写时可以提高性能。
dbm 模块
    简介：
        dbm是一个通用的接口，用于访问不同类型的数据库文件，它是一组简单的键值存储数据库接口的集合。
        Python 标准库中包含了多个dbm的具体实现，如dbm.gnu（基于 GNU dbm 库）、dbm.ndbm等，不同实现可能在功能和性能上略有差异。
    特点
        底层接口：相比 shelve，dbm更接近底层，更注重基础的键值对存储操作，灵活性更高。
        数据类型限制：dbm主要用于存储简单的字符串键值对，存储的值需要是字节串形式。如果要存储复杂的 Python 对象，需要先进行序列化（如使用pickle模块）。
        性能和可移植性：不同的dbm实现可能在性能和可移植性上有差别，比如dbm.gnu在 GNU/Linux 系统上表现良好，选择合适的实现对于不同的运行环境很重要。
'''
    # import shelve
    # shelFile=shelve.open('mydata')
    # cats=['Zophie','Pooka','Simon']
    # shelFile['Cats']=cats
    # shelFile.close()

    # print(shelFile['Cats'])
    # shelFile.close()          #使用close关闭文件之后下面的list(shelFile.keys()),list(shelFile.values())会无法正常运行 因为已经关闭了文件
    # print(type(shelFile.close()))

    # print(list(shelFile.keys()))
    # print(list(shelFile.values()))
    # shelFile.close()

#用 pprint.pformat()函数保存变量
    import pprint
    # cats=[{'name':'px','desc':'student'},{'name':'hdf','desc':'workmen'}]
    # print(pprint.pformat(cats))
    # print(type(pprint.pformat(cats)))
    #
    # fileObj=open('myCatsl.py','w')
    # fileObj.write(f'cats={pprint.pformat(cats)}\n')
    # fileObj=open('myCatsl.py','r')
    # print(fileObj.read())
    #
    # fileObj=open('myCatsl.py','w')
    # fileObj.write(f'cats={cats}\n')
    # fileObj=open('myCatsl.py','r')
    # print(fileObj.read())
    #
    # fileObj.close()

    # import myCatsl
    # print(myCatsl.cats)
    # print(myCatsl.cats[0])
    # print(myCatsl.cats[0]['name'])