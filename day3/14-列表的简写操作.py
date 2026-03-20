a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(f'数据{a},地址{id(a)}')
print(a * 2)
a.extend(b)
print(f'操作后,数据{a},地址{id(a)}')
print(a + b)
a += b  # 等价于extend,和a=a+b是不一样的
print(f'操作后,数据{a},地址{id(a)}')
