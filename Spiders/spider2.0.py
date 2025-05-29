# 发送请求
#pip install requests
import time
from operator import truediv
import requests
#pip install lxml
from lxml import etree

# 发送给谁
url = "http://www.jianlaixiaoshuo.com/book/17.html"  # 笔趣阁剑来小说
end="第一千二百一十八章 看书人"#终止循环
while True:
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'#进行伪装
    }
    # 发送请求
    resp=requests.get(url,headers=headers)
    # 设置编码
    resp.encoding='utf-8'
    # 响应请求
    # print(resp.text)

    e=etree.HTML(resp.text)
    info='\n'.join(e.xpath('//*[@id="BookText"]/p/text()'))
    title=e.xpath('string(//div/h1)')
    url=f'http://www.jianlaixiaoshuo.com{e.xpath('//*[@id="BookCon"]/div[1]/a[3]/@href')[0]}'

    print(title)
    # print(info)
    # print(url)

    # 保存路径

    with open(r'C:\Users\31874\Desktop\剑来\剑来.txt','a',encoding='utf-8') as f:
        f.write(title+'\n\n'+info+'\n\n')
    time.sleep(2)
    '''
    退出循环
    '''
    if title == end:
        print('小说遍历完毕')
        break
