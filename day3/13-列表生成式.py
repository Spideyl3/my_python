my_list = [x for x in range(10)]
print(my_list)
# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
# 二维列表
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
print(a[2][3])
a = [j for x in a for j in x]  # 2维列表转1维列表
print(a)
# 只有if时
a = [x for x in range(10) if x % 2 == 0]  # 将只会筛选偶数
print(a)
# if-else的三元表达式

a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)
