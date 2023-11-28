a = ["我", "你"]
b = ["Love", "?"]

print(list(zip(a, b)))

for i, j in zip(a, b):
    print(i, j, end="", sep="")


# zip  类元组对象
#      可解包
