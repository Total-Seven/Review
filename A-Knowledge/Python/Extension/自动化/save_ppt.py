from PIL import Image
import pyautogui as pag
import time
import keyboard
import sys

DELAY_TIME = 0.35
BESTKEY = "space"
flag = 0
count = 0
time.sleep(2)
# print(pag.position())


pag.press("f11")
pag.moveTo(1298,729,0.25)
pag.click()



def escape(event):
    global flag
    esc = keyboard.KeyboardEvent("down",28,"esc") # 退出键
    if event.event_type == "down" and event.name == esc.name:
        print("exit!")
        flag = 1
        sys.exit()
        exit()


keyboard.hook(escape)



time.sleep(1)

while True:
    if flag:
        break
    
    count += 1
    
    img = pag.screenshot()
    imgName = f'{count}.jpg'
    img.save(f"E:\ppt\{imgName}") # 保存目录
    pag.press(BESTKEY)
    
    time.sleep(DELAY_TIME)
    

