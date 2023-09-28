import keyboard
import sys
import time


flag = 0


def cb(x):
    global flag
    print(x)
    a = keyboard.KeyboardEvent("down",28,"esc")
    if x.event_type == "down" and x.name == a.name:
        flag = 1
        sys.exit()
        exit()


keyboard.hook(cb)
    

while True:
    if flag:
        break
    print("666")
    time.sleep(1)
