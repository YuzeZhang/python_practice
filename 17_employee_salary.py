


import sys
employee_num = 0
average_salary = 0
sum_salary = 0
list = []
#主界面
def main():
    print('*'*50)
    print('请输入要选择的功能:')
    print('1:录入员工薪资')
    print('2:显示薪资明细')
    print('3:退出程序')
    print('*'*50)
    select = int(input())
    if select==1:
        infor_get()
    elif select==2:
        infor_out()
    elif select==3:
        sys.exit()
    else:
        print('输入错误，请重新输入')
        main()
#平均薪资计算函数
def calculate():
    global sum_salary
    global average_salary
    for i in list:
        sum_salary=i+sum_salary
    average_salary=sum_salary/employee_num
#员工信息录入函数
def infor_get():
    global list
    global employee_num
    global sum_salary
    #list.append(int(input('请输入您的薪资')))
    salary = int(input('请输入您的薪资:'))
    if salary<0:
       print('请重新输入')
    elif salary>=0:
       list.append(salary)
    else:
        print('请重新输入')
    employee_num+=1
    sum_salary=0
    calculate()
    main()
#打印函数
def infor_out():
    print('员工数量为：%d'%employee_num)
    print('平均薪资为:%d'%average_salary)
    print('薪资总数为:%d'%sum_salary)
    print('薪资明细:')
    print(list)
    main()
main()
