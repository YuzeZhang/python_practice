


#获取(x,y)的值
x = int(input('请输入x的值'))
y = int(input('请输入y的值'))



tup = (x,y)
if tup[0]>0:
    if tup[1]>0: 
        print('(x,y)处于第一象限')
    else:
        print('(x,y)处于第四象限')
else:
    if tup[1]>0:
        print('(x,y)处于第二象限')
    else:
        print('(x,y)处于第三象限')










