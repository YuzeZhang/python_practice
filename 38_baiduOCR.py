from  aip import AipOcr
from PIL import Image

#API信息
APP_ID = 'e466d3130c5743bcadad7f2b41b9145b'
API_KEY = '3bc8c792550e4e3983b651603d0005f8'
SECRET_KEY = '7ccdd7deb176477f85b5fdd0448a654e'

#新建AipOcr
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)


#处理图片
size = (400,100)
with open('code.jpg','rb') as fp:
    image = Image.open(fp=fp)
    print(image.size)
    out = image.resize(size,Image.ANTIALIAS)
    print(out.size)
    out.save('code_processed.jpeg','jpeg')

#读取图片
def get_image():
    with open('code_processed.jpeg','rb') as fp:
        return fp.read()

image2 = get_image()
#调用文字识别
result = client.basicGeneral(image2)

words
words_list = result.get('words_result')
for item in words_list:
    words_dict = item
print(result.get('words_result'))
#print(words_dict.get('words'))
