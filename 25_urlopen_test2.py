import urllib.request

url = 'http://zhangyuzechn.cn'
response = urllib.request.urlopen(url = url)
print(response.read().decode())
