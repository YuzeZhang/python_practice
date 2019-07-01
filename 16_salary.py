


dict1 = {'name':'高小一','age':18,'salary':30000}
dict2 = {'name':'高小二','age':19,'salary':20000}
dict3 = {'name':'高小五','age':20,'salary':10000}
list = [dict1,dict2,dict3]
for i in list:
    if i.get('salary')>15000:
        print(i)
