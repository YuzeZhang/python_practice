import urllib.request


url = r'http://218.60.144.59/imgchk/validatecode.asp?r=Sun%20Aug%2018%202019%2021:45:44%20GMT+0800%20(%D6%D0%B9%FA%B1%EA%D7%BC%CA%B1%BC%E4)'
#伪装请求头
headers = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection' : 'keep-alive',
    'Cookie': 'ASPSESSIONIDAQRDBBDS=HKLDEIIALPGFOCMLMIGGNIHE; tkt=tktda=&tkts=; jdt=jdtda=&jdts=; pdt=pdtda=&pdts=; xzt=xztda=&xzts=; dxz=dxzda=&dxzs=; ajj=lx=2&zx=2; zx=zkzh=110101199003077432&bh=&id=&examid=&wdt=&name1=&idcard=&kssj=&jssj=&dqth=',
    'Host': '218.60.144.59',
    'Referer': 'http://218.60.144.59/mnzxlogin.asp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
#构建请求对象
request = urllib.request.Request(url=url,headers=headers)
#发送请求
response = urllib.request.urlopen(request)

with open('code.jpg','wb') as fp:
    fp.write(response.read())