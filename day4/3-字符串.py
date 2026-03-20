def check_type():
    """
    判断字符串类型
    :return:
    """
    s1 = 'abc*'
    print(s1.isalnum())
    s2 = '123'
    print(s2.isdecimal())


def str_find():
    """
    字符串查找
    :return:
    """
    s1 = 'abcdefg'
    print(s1.find('cd', 1))
    s2 = s1.replace('cd', 'CD', 1)  # 第三个参数控制替换次数
    print(s2)


def str_split_join():
    """
    字符串分割与连接
    :return:
    """
    s1 = 'abc bcd'
    print(s1.split())
    s1 = 'abc,bcd'
    print(s1.split(','))
    s2 = 'abc\nbcd\nefg'
    print(s2.splitlines())
    str_list = ['a', 'b', 'c', 'd']
    print(str_list)
    print(','.join(str_list))


if __name__ == '__main__':
    check_type()
    str_find()
    str_split_join()
