list = [-1, 0, 1, 2, 3]

f_list = filter(lambda i: i > 0, list)

print(f_list)  # <filter object at 0x00000204B22B6A10>

for i in f_list:
    print(i)
'''
1
2
3
'''
