#这是本项目正儿八经的第一个项目，使用多剪切板达到回复消息的作用
import sys,pyperclip
TEXT={'agree':'''我同意，我过会去找你''',
      'busy':'''不好意思，我这几天很忙''',
      'upsell':'''我会考虑一下你的提议'''}
if len(sys.argv) < 2:
      print('使用方法：python filename [keyphrase] - 要加入命令参数')
      sys.exit()
keyphrase=sys.argv[1]
# print(keyphrase)
if keyphrase in TEXT:
      pyperclip.copy(TEXT[keyphrase])
      print('文本内容已经拷贝到剪切板')
else:
      print(f'没有这个选项:{keyphrase}')