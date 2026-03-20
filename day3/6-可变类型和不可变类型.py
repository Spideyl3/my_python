def no_change(num):
    print(f'num={num}, id={id(num)}')
    num = 5
    print(f'修改num后，num={num}, id={id(num)}')


a = 10
print(f'调用函数前a的地址{id(a)}')
no_change(a)
print(f'调用函数后a的值{a}')


def change(new_list):
    print(f'赋值前,new_list的地址{id(new_list)}')
    new_list[0] = 10
    print(f'修改new_list后,new_list的地址{id(new_list)}')


my_list = [1, 2, 3]  # 可变类型
print(f'调用函数前{my_list}的地址{id(my_list)}')
print(f'调用函数前{my_list}')
change(my_list)
print(f'调用函数后{my_list}')
print(f'调用函数后{my_list}的地址{id(my_list)}')