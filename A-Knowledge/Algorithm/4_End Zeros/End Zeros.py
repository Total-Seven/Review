def endZeros(n):
    if n == 0:
        return 1

    res = 0
    while not n % 10:
        res += 1
        n //= 10
    return res


print(endZeros(0))
print(endZeros(1))
print(endZeros(10))
print(endZeros(101))
print(endZeros(245))
print(endZeros(100100))

# endZeros(0), 1)
# endZeros(1), 0)
# endZeros(10), 1)
# endZeros(101), 0)
# endZeros(245), 0)
# endZeros(100100), 2)
