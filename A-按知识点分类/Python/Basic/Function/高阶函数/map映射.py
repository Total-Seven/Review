'''
  map
    功能: 将可迭代对象的每个元素作为函数参数执行
    返回值: map对象
    参数: fn、可迭代对象
'''


# 给每个元素的末尾都加上日期
date = " 2023-10-09"
list = ["11", "22", "33"]
for i in range(len(list)):
    list[int(i)] += date

print(list)



# Python中字符串是不可变的
# 如果要修改列表内的字符串
# 需要通过索引
