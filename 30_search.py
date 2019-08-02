import urllib.request
import urllib.parse

word = input('请输入想要搜索的内容：')
url = 'http://www.baidu.com/s?'

#将参数写成一个字典
data = {
    'ie':'utf-8',
    'wd':word,
}

#将参数加入url中
query_string = urllib.parse.urlencode(data)
url += query_string

#发送请求
response = urllib.request.urlopen(url=url)

#生成文件并将搜索页面保存进文件中
filename = word+'.html'
with open(filename,'wb') as fp:
    fp.write(response.read())
