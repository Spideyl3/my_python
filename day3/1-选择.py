import random

# 1.定义年龄变量
age = 17;
# 2.判断是否满18岁
if age >= 18:
    print('happy')
else:
    print('go home')


def use_elif():
    holiday_name = "平安夜"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日!")


def use_two_if():
    has_ticket = True
    knife_length = 20
    if has_ticket:
        print("可以开始安检")
        if knife_length >= 20:
            print("不允许携带%d厘米长的刀" % knife_length)
        else:
            print("安检通过")
    else:
        print("先买票再来")


def use_random():
    player = int(input("请出拳 石头(1)/剪刀(2)/布(3):"))
    # 固定
    computer = 1;
    # 随机
    # randint()闭区间
    computer = random.randint(1, 3)
    print(player, computer)

    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):
        print("你赢了")
    elif player == computer:
        print("平局")
    else:
        print("你输了")


use_elif()
use_two_if()
use_random()
