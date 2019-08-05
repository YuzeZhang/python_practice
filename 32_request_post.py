import urllib.request
import urllib.parse

word = input("请输入要查询的单词:")
#获取post_url的地址
post_url = 'http://fanyi.baidu.com/sug'
#构建表单数据
form_data = {
    'kw':word
}
#伪装头部信息
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url=post_url,headers=headers)
#处理表单数据
form_data = urllib.parse.urlencode(form_data).encode()
#发送请求
response = urllib.request.urlopen(request,data=form_data)
#打印结果
print(response.read().decode())
