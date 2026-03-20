def say_hello():
    print('hello 1')
    print('hello 2')
    print('hello 3')


# print('函数执行前')
# say_hello()
# print('函数执行后')

def sum_2_num(num1, num2):
    """
    num1和num2是形参
    :param num1:
    :param num1:
    :param num2:
    :return:
    """
    result = num1 + num2
    print(f'求和结果{result}')
    return result


ret = sum_2_num('abc', 'efg')
print(ret)
