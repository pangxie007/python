from time import sleep

import requests
from lxml import etree
# 目标地址
url = "http://www.jianlaixiaoshuo.com/book/17.html"
# 伪装池
Headers_1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (kHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
}
Headers_2 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
# 循环遍历到小说结束
start_title = ''
end_title = "第一千二百一十八章 看书人"
a=0
while start_title != end_title:
    resp = requests.get(url, headers=Headers_2)
    resp.encoding = 'utf-8'
    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//*[@id="BookText"]/p/text()'))
    start_title = e.xpath('string(//div/h1)')
    url = f'http://www.jianlaixiaoshuo.com{e.xpath('//*[@id="BookCon"]/div[1]/a[3]/@href')[0]}'
    print(start_title)
    sleep(0.8)
    # 保存文件
    with open(r'C:\Users\31874\Desktop\剑来\剑来.txt', 'a', encoding='utf-8') as f:
        f.write(start_title + '\n\n' + info + '\n\n')
    a+=1
    if a==100:
        resp = requests.get(url, headers=Headers_1)
        print("已经转换")
        resp.encoding = 'utf-8'
        e = etree.HTML(resp.text)
        info = '\n'.join(e.xpath('//*[@id="BookText"]/p/text()'))
        start_title = e.xpath('string(//div/h1)')
        url = f'http://www.jianlaixiaoshuo.com{e.xpath('//*[@id="BookCon"]/div[1]/a[3]/@href')[0]}'
        print(start_title)
        sleep(0.8)
        with open(r'C:\Users\31874\Desktop\剑来\剑来.txt', 'a', encoding='utf-8') as f:
            f.write(start_title + '\n\n' + info + '\n\n')
        a+=1
        if a==200:
            a=0
            continue