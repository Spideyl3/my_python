def use_while1():
    # 1.定义重复次数计数
    i = 1

    # 2.使用while 判断条件
    while i <= 5:
        # 要重复执行的代码
        print("Hello Python")

        # 处理计数器i
        i = i + 1

    print(f'循环结束,i的值{i}')
    print("循环结束后的 i = %d" % i)


def use_continue():
    # 计算 0 ~ 100 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:

        if i % 2 == 1:
            i += 1
            continue
        # 每一次循环，都让 result 这个变量和 i 这个计数器相加
        result += i

        # 处理计数器
        i += 1

    print("0~100 之间的数字求和结果 = %d" % result)
    print(f"0~100 之间的数字求和结果 = {result} i={i}")


def use_break():
    # 计算 0 ~ 100 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:

        if result > 2000:
            break
        # 每一次循环，都让 result 这个变量和 i 这个计数器相加
        result += i

        # 处理计数器
        i += 1

    print("0~100 之间的数字求和结果 = %d" % result)
    print(f"0~100 之间的数字求和结果 = {result} i={i}")


def use_print():
    print("hello", end='')  # 不要换行
    print("hello", end=' ');  # 加空格
    print("hello", end='\n');  # 换行


def use_for():
    my_list = ['ab', 'bd', 'cf']
    print(my_list[0])
    for i in my_list:
        print(i, end=' ')
    print()
    print('-' * 50)
    print(i)


def use_for_range():
    for i in range(10):  # 0~9(左闭右开)
        if i == 15:
            print(f'find{i}')
            break
    else:
        print('not found')


use_while1()
use_continue()
use_break()
use_print()
use_for()
use_for_range()
