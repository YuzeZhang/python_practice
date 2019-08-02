url = 'http://www.baidu.com/index.html'

name = 'zhangsan'
age = 18
sex = 'male'
height = '180'

data = {
    'name':name,
    'age':age,
    'sex':sex,
    'height':height
}

list = []
for k,v in data.items():
    list.append(k + '=' + str(v))
query_string = '&'.join(list)
url = url +'?' + query_string
print(url)