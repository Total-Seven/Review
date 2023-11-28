"""
2
15A6F
1011

"""

"""
二 八 十进制 十六

"""

import re
n = input()
res = [0] * 4

Hex = re.search(r"[A-F]", n)
Dec = re.search(r"[8-9]", n)
Oct = re.search(r"[2-7]", n)
Bin = re.search(r"[0-1]", n)

if Hex:
    res[3] = 1
elif Dec:
    res[2] = res[3] = 1
elif Oct:
    res[1] = res[2] = res[3] = 1
elif Bin:
    res[0] = res[1] = res[2] = res[3] = 1

print(res)
