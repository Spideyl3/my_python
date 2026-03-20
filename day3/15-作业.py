def homework4():
    # 实现从1到100的奇数求和
    print([x for x in range(101) if x % 2 == 1])


def homework5():
    """
    九九乘法表
    :return:
    """
    for i in range(10):  # 外层控制行
        for j in range(1, i + 1):  # 内层控制列
            print(f'{j}*{i}={j * i < 2}', end=' ')  # 左对齐是<
        print()


def homework6():
    """
    统计1的个数
    :return:
    """
    s = int(input("请输入一个正整数："))
    if s >= 0:
        num = bin(s).count('1')
    else:
        num = 64 - bin(-s - 1).count('1')
    print(num)


def homework2():
    """
    位运算实现
    :return:
    """
    s = int(input("请输入一个正整数："))
    check_bit_flag = 1
    count = 0
    while check_bit_flag < 2 ** 64:
        if check_bit_flag & s:
            count += 1
        check_bit_flag <<= 1
    print(count)


if __name__ == '__main__':
    homework4()
    homework5()
    homework6()
    homework2()
