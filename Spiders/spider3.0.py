"""
由于2.0爬取过程中总是出现中断 以目前技术无法确定原因
第三版更新为每获取100-200章休眠一段时间或者使用另一个header
"""
import time
from math import trunc
from operator import truediv
import requests
from lxml import etree

url = "http://www.jianlaixiaoshuo.com/book/17.html"  # 笔趣阁剑来小说剑来第一章
end="第一千二百一十八章 看书人"#终止循环 条件
# '''
# 退出循环
# '''
# if title == end:
#     print('小说遍历完毕')
#     break
while True:
    for i in range(1,151):
        #伪装poor 第一个100轮使用第一个 第二个100轮使用第二个
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (kHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
        }
        headers_2={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
        }
        #伪装轮询
        check_rang=150/i
        if check_rang==1:
            print("进入第二次for循环，切换伪装")
            check_rang=0
            resp = requests.get(url, headers=headers_2)
