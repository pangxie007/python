#利用webbrowser模块的maplt.py
"""
项目不完整 书中的内容不够入门 时间过久对比现在python爬虫来说不是一个很好的入门项目
"""
"""这个程序主要是利用输入参数和剪切板中的google地图地址 进行google地图的跳转
   如果是以参数形式输入地址 则需要加双引号
   以剪切板形式输入地址 则不用
"""
    # import webbrowser,sys,pyperclip,logging,urllib.parse
    # logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
    #
    # logging.debug(f'接收到的参数长度为：{len(sys.argv)}')
    # logging.debug(f'参数地址为：{sys.argv[1:]},转换后为：{''.join(sys.argv[1:])}')
    # logging.debug(f'剪切板中的内容为：{pyperclip.paste()}')
    #
    # #输入判断
    # if len(sys.argv) > 1:
    #     webbrowser.open(rf'https://www.google.com/maps/{''.join(sys.argv[1:])}')
    # elif len(sys.argv) == 1:
    #     webbrowser.open(rf'https://www.google.com/maps/{pyperclip.paste()}')

#用requests模块从web下载文件
    # import requests
    # res=requests.get(r"https://requests.readthedocs.io/en/latest/")
    # print(type(res))
    # print(res.status_code)
    # print(res.status_code == requests.codes.ok)
    # print(len(res.text))
    # print(res.text[:50])
    # print(requests.codes.ok)

#检擦错误
    # import requests
    #
    # try:
    #     res = requests.get(r"https://requests.readthedocs.io/en/latest/asdsadasdadsd")
    #     res.raise_for_status()
    # except Exception as exc:
    #     print(f'出现报错{exc}\n但是被忽略')

#将下载的文件保存到硬盘
"""这里必须使用二进制来进行数据的保存，这样做的目的是保存文本中的 Unicode编码"""
    # import requests
    # res=requests.get(r"https://docs.python.org/zh-cn/3/library/webbrowser.html#module-webbrowser")
    # res.raise_for_status()
    # savePath=open(r"D:\python\project\FunctionTest\从web抓取信息测试目录\web_content.txt",'wb')
    # for i in res.iter_content(100000):
    #     savePath.write(i)
    # savePath.close()

#HTML 略

#用bs4 模块解析 HTML
    # import requests,bs4
    # res=requests.get(r"https://weather.cma.cn/web/weather/57476")
    # res.raise_for_status()
    # noStarchSoup=bs4.BeautifulSoup(res.text,'html.parser')
    # print(type(noStarchSoup))
    # content=noStarchSoup.select('#temperature')
    #
    # print(content)

#从HTML创建一个BeautifulSoup对象
    # import requests,bs4
    # wsPath=open(r"D:\python\project\FunctionTest\从web抓取信息测试目录\websit.html")
    # wsSoup=bs4.BeautifulSoup(wsPath,'html.parser')
    # print(type(wsSoup))
    # # print(wsSoup.prettify())
    # content=wsSoup.select('#author')
    # print(type(content))
    # print(len(content))
    #
    # print(content)
    # print(content[0])
    # print(str(content))
    # print(content[0].getText())
    # print(content[0].attrs)
    #
    # content=wsSoup.select('p')
    # print(content)
    # print(str(content))
    # print(str(content[0]))
    # print(str(content[0].getText()))
    # print(str(content[1]))
    # print(str(content[1].getText()))
    # print(str(content[2]))
    # print(str(content[2].getText()))

#通过元素的属性获取数据
    # import bs4
    # soup=bs4.BeautifulSoup(open(r'D:\python\project\FunctionTest\从web抓取信息测试目录\websit.html'),'html.parser')
    # a=open(r'D:\python\project\FunctionTest\从web抓取信息测试目录\websit.html')
    # print(type(a))
    # print(soup.select('span'))
    # print(soup.select('span')[0])
    # print(type(soup.select('span')[0]))
    #
    # print(str(soup.select('span')[0]))
    # print(type(str(soup.select('span')[0])))
    #
    # spanElem=soup.select('span')[0]
    # print(spanElem.get('id'))
    # print(spanElem.get('some_nonexistent_addr') == None)
    # print(spanElem.attrs)

#打开所有搜索结果
    # import sys,requests,webbrowser,logging,bs4
    #
    #
    # res=requests.get(rf"https://cn.bing.com/search?q={ ' '.join(sys.argv[1:])}")
    # res.raise_for_status()
    # print( ' '.join(sys.argv[1:]))
    # print(res.url)
    # print(res.text)
    #
    # resSoup=bs4.BeautifulSoup(res.text,'html.parser')
    # Soup=resSoup.select('h2')

    # for i in range(len(Soup)):
    #     print(Soup[i])