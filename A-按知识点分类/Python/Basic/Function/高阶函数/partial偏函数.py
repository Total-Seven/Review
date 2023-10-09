from functools import partial
# 偏函数  固定参数
number = '0x0f'
print(int(number, base=16))

int_16 = partial(int, base=16)

print(int_16(number))
