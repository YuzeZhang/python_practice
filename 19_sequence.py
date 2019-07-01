


n = int(input('请输入n的值:'))
num = 0
sum = 0
for i in range(0,n+1):
    num = float(i/(i+1))
    sum+=num
print('结果为：%f'%sum)
