#coding=utf-8


i = 1
list1 = []
list2 = []
list3 = []
while i<100:
    list1.append(i)
    if i%2==0:
        list2.append(i)
    else:
        list3.append(i)
    i+=1
result1=result2=result3=0
for num in list1:
    result1+=num
print("1-100数字的和为%d"%result1)
for num in list2:
    result2+=num
print('1-100偶数的和为%d'%result2)
for num in list3:
    result3+=num
print('1-100奇数的和为%d'%result3)
