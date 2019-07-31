import urllib.request

url = 'http://zhangyuzechn.cn'
response = urllib.request.urlopen(url = url)

with open('zhangyuze.html','w',encoding='utf-8') as fp:
    fp.write(response.read().decode())