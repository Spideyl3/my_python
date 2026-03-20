xiaoming_dict = {'name': '小明'}
# 1.取值
print(xiaoming_dict['name'])

# 2.增加,修改
xiaoming_dict['age'] = 20
print(xiaoming_dict)

# 如果key存在.会修改已存在的键值对
xiaoming_dict['name'] = '小小明'
print('-' * 50)
print(xiaoming_dict)

# 3.删除
# print(xiaoming_dict.pop('name'))
del xiaoming_dict['name']
print(xiaoming_dict)

# 4.统计键值对的数量
print(len(xiaoming_dict))

# 5.合并字典
temp_dict = {'height': 1.75, 'age': 20}

xiaoming_dict.update(temp_dict)
print('-' * 50)
print(xiaoming_dict)

# 3. 清空字典
xiaoming_dict.clear()
print('-' * 50)
print(xiaoming_dict)

# 4.遍历字典
print('-' * 50)
xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print(k, xiaoming_dict[k])
print('-' * 50)
for k, v in xiaoming_dict.items():
    print(f'键{k},值{v}')
for k in xiaoming_dict.keys():
    print(f'键{k}')
for v in xiaoming_dict.values():
    print(f'值{v}')

card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:
    print(card_info)
if __name__ == '__main__':
    k, v, w = (1, 2, 3)
    print(k, v, w)
