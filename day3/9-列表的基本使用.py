name_list = ["zhangsan", "lisi", "wangwu"]
# 1.取值
print(name_list[0])
# 查找元素
print(name_list.index('wangwu'))

# 2.修改元素
name_list[1] = '李四'
print(name_list)

# 3.添加
name_list.append('王五')
print(name_list)

name_list.insert(1, '王小美')
print(name_list)
temp_list = ['孙悟空', '猪二哥', '沙师弟']
name_list.extend(temp_list);
print(name_list)

# 4.删除
# remove()方法删除指定元素，如果元素不存在，则会报错
name_list.remove('wangwu')
# pop()方法默认可以把列表最后一个元素删除
# name_list.remove('zhangsan')
# # pop(index)方法可以删除指定位置的元素
# name_list.pop(1)
# # clear()方法可以清空列表
# name_list.clear()
# del name_list
print(name_list)
