import random as r
teacher = ["张老师", "林老师", "刘老师", "王老师"]

course = set()

res = dict.fromkeys(teacher)

index = 0
while index < 4:
    number = r.randint(1, 4)
    if number not in course:
        course.add(number)
        res[teacher[index]] = number
        index += 1

print(res)
