import turtle as t

t.pensize(1)
t.fillcolor("green")
t.pencolor("black")
t.shape("turtle")


"""
(0, 0)    (200,0)
(0, -200)    (200,-200)

"""
for i in range(4):
    t.fd(200)
    t.right(90)

point = tuple(map(int, t.textinput("坐标", "请输入海龟要去的位置坐标(x,y)").split(",")))
x, y = point
t.penup()
t.goto(int(x), int(y))


def where(point):
    match point:
        case (0, 0):
            print("在左上角")
        case (0, -200):
            print("在左下角")

        case (200, 0):
            print("在右上角")
        case (200, -200):
            print("在右下角")

        case (x, 0) if 0 <= x < 200:
            print("在上边")
        case (x, -200) if 0 <= x < 200:
            print("在下边")
        case (0, y) if -200 < y < 0:
            print("在左边")
        case (200, y) if -200 < y < 0:
            print("在右边")

        case (x, y) if 0 < x < 200 and -200 < y < 0:
            print("在里面呢！")
        case _:
            print("在外面呢！")


t.onkey(where(point), 'Up')
t.listen()


t.mainloop()
t.done()
