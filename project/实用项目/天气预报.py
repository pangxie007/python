import requests,json
#定义网页路径
url=r'https://weather.cma.cn/api/now/57476'

#获取网页JSON数据
res=requests.get(url)
res.raise_for_status()

#将json数据装换成python字典
jsonData=json.loads(res.text)
# print(jsonData)

#打印天气数据
print(rf"城市:{jsonData['data']['location']['path']}")
print(rf"温度:{jsonData['data']['now']['temperature']}")
print(rf"风速:{jsonData['data']['now']['windDirection']}_{jsonData['data']['now']['windScale']}")
print(rf"空气湿度:{jsonData['data']['now']['humidity']}")
print(rf"大气压:{jsonData['data']['now']['pressure']}")