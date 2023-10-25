import numpy as np
# 1
# a = np.array([[1, 2], [3, 4]])
# print(a)
# 2
# dt = np.dtype("i4")
# print(dt)
# 3
# dt = np.dtype(['age', np.int8])
# a = np.array([(10,), (20,), (30,)], dtype=dt)
# print(a["age"])
# 4
a = np.arange(8)
print(a)

b = np.array([1, 2, 3, 4, 5], ndmin=2)
print(b)
