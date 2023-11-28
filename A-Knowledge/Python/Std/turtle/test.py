import turtle
import keyboard
# 创建海龟对象
t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)


def square():
    t.color("blue", "green")
    """ 正方形 """
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    for i in range(4):
        t.fd(200)
        t.right(90)
    t.color("black", "green")


def where(point):
    match point:
        case (-100, 100):
            print("在左上角")
        case (-100, -100):
            print("在左下角")

        case (100, 100):
            print("在右上角")
        case (100, -100):
            print("在右下角")

        case (x, y) if -99 < x < 99 and 95 <= y <= 105:
            print("在上边")
        case (x, y) if -99 < x < 99 and -105 < y < -95:
            print("在下边")
        case (x, y) if -99 < y < 99 and - 105 < x < -95:
            print("在左边")
        case (x, y) if -99 < y < 99 and 95 < x < 105:
            print("在右边")

        case (x, y) if -99 < x < 99 and -99 < y < 99:
            print("在里面呢！")
        case _:
            print("在外面呢！")


def move(direction):
    # 设置海龟的朝向
    if direction == "Up":
        t.setheading(90)
    elif direction == "Down":
        t.setheading(270)
    elif direction == "Left":
        t.setheading(180)
    elif direction == "Right":
        t.setheading(0)

    # 移动海龟
    t.forward(1)
    where(t.pos())


square()
# 监听键盘事件
turtle.listen()

# 设置键盘事件绑定
keyboard.on_press_key("up", lambda e: move("Up"))
keyboard.on_press_key("down", lambda e: move("Down"))
keyboard.on_press_key("left", lambda e: move("Left"))
keyboard.on_press_key("right", lambda e: move("Right"))

# 进入主循环
turtle.mainloop()
