def use_tuple():
    # 1.构造元组
    info_tuple = ("zhangsan", 18, 1.75)
    for i in info_tuple:
        print(i)

    print('-' * 50)
    print(info_tuple.index('zhangsan'))
    # 2.统计计数
    print(info_tuple.count('zhangsan'))
    # 统计元组中包含元素的个数
    print(len(info_tuple))


def use_str():
    info_tuple = ("小明", 21, 1.85)

    # 格式化字符串后面的`()` 本质上就是元组
    print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

    info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
    print(info_str)
    print(f'使用f{info_tuple}')


if __name__ == '__main__':
    use_tuple()
    use_str()
