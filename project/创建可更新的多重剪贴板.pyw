"""
mcb.pyw 存储剪切板内容
python filename save [name]   将剪切板的内容用[name]关键字存储在mcb.pyw中
python filename [name]        将存储的[name]从mcb.pyw中读取出来存放到剪切板中
python filename list          列出所有可用关键字
python filename del           清空mcb中存储的所有值
python filename del [name]    删除mcb中指定的[name]关键字
"""
import sys,pyperclip,shelve
mcbShelf=shelve.open('mcb')
#输入错误控制【扫盲】
if len(sys.argv) > 3:
      print('使用方法：python filename list 查看可用关键字')
      sys.exit(127)
k={}
#将指令传递给变量存储
if len(sys.argv)==3 and sys.argv[1].lower() == 'save':
      mcbShelf.setdefault(sys.argv[2].lower(),pyperclip.paste())
elif len(sys.argv)==2 and sys.argv[1].lower() == 'list':
      pyperclip.copy(list(mcbShelf.keys()))
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
      del mcbShelf[sys.argv[3]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'del':
      for i in list(mcbShelf.keys()):
            del mcbShelf[i]
elif len(sys.argv)==2:
      if sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])
      else:
            print('这个关键字不在存储库中！')

# print(len(sys.argv))
# print(sys.argv[1])
# print(list(mcbShelf))
# print(list(mcbShelf.values()))


mcbShelf.close()