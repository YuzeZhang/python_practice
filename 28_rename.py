import os
path = r'E:\git_c_practice\c_practice\\'
for file in os.listdir(r'E:\git_c_practice\c_practice'):
    str = file[:2]
    print(str)
    if file[-2: ]=='md':
        continue
    if (file[:2]>='13') and (file[:2]<='99'):
        name = path+file
        new_name = path+'0'+file
        os.rename(name,new_name)