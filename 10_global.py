

#定义一个全局变量
wendu = 0
def get_wendu():
    global wendu
    wendu = 27
def print_wendu():
    print(wendu)
get_wendu()
print_wendu()
