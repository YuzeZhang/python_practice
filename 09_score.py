


#获取分数
score = int(input('请输入你的分数(0-100)'))

if score >= 90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
elif score>=60 and score<70:
    print('D')
elif score>=0 and score<60:
    print('E')
else:
    print('输入错误')
