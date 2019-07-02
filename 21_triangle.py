

import math
#计算三角形面积
def area():
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('三角形面积为:%f'%s)
#获取三个顶点坐标
x1,y1 = eval(input('请输入第一个坐标，以逗号隔开:'))
x2,y2 = eval(input('请输入第二个坐标，以逗号隔开:'))
x3,y3 = eval(input('请输入第三个坐标，以逗号隔开:'))
#计算三条边长
a = float(math.sqrt(math.pow((x2-x3),2)+math.pow((y2-y3),2)))
b = float(math.sqrt(math.pow((x1-x3),2)+math.pow((y1-y3),2)))
c = float(math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2)))

#判断是否有效
if a+b>c and a+c>b and b+c>a:
    area()
else:
    print('该坐标无效，不能构成三角形')


