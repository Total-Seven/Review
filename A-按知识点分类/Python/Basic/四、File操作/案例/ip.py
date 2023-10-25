with open("ip.txt", "r") as f:
    # 每次读取一行数据
    list = f.readlines()
    for i in range(0, len(list)):
        list[i] = list[i].strip('\n')
    for i in range(len(list)-1, -1, -1):
        # for i in list[::-1]:
        # for i in list:
        print(list[i])

# f = open("ip.txt", "r+")
# strr = f.read()
# print(strr)
