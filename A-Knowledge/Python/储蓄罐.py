"""

I:2 3
O:0 1 0

-----------

I:3 5
O:0 0 0 2 0

"""
numOfJaries = list(map(int, input().split(" ")))[0]
jar_index_list = list(map(int, input().split(" ")))

jar = [0]*numOfJaries

for i, jar_index in enumerate(jar_index_list):
    jar[jar_index] += i+1

print(jar)
