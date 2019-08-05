from bs4 import BeautifulSoup
import urllib.request

url = 'http://zhangyuzechn.cn'

response = urllib.request.urlopen(url= url)

content = response.read()
soup = BeautifulSoup(content,'html.parser')