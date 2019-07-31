import urllib.request

image_url = 'https://user-gold-cdn.xitu.io/2019/2/24/1691d8e383f30621?imageView2/0/w/1280/h/960/format/webp/ignore-error/1'
response = urllib.request.urlopen(image_url)
with open('image.jpg','wb') as fp:
    fp.write(response.read())