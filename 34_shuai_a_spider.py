from bs4 import BeautifulSoup
import urllib.request
import os

list_target = []
print('正在采集图片链接...')
for num in range(1,3):
    if num == 1:
        url = 'http://www.shuaia.net/oumei/index.html'
    else:
        url = 'http://www.shuaia.net/oumei/index_%d.html'%num
    #伪装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    #构建请求对象
    request = urllib.request.Request(url=url,headers=headers)

    #发送请求
    response = urllib.request.urlopen(request)
    html = response.read().decode()
    #beautiful soup处理
    soup = BeautifulSoup(html,'lxml')
    target = soup.find_all(class_='itemimg-view')

    #数据导入列表
    for each in target:
        list_target.append(each.get('title') + '=' +'http://www.shuaia.net'+ each.get('href'))
print('图片链接采集完成！')
for each_img in list_target:
    img_info = each_img.split('=')
    file_name = img_info[0] + '.jpg'  #图片文件名
    img_target = img_info[1]   #图片地址
    '''
    img_response = urllib.request.urlopen(img_target)
    with open('%s'%file_name,'wb') as fp:
        fp.write(response.read())
    '''
    if 'images' not in os.listdir():
        os.makedirs('images')
    print('正在下载'+file_name+'...')
    urllib.request.urlretrieve(url = img_target,filename = 'images/' + file_name)
print('下载完成!')
