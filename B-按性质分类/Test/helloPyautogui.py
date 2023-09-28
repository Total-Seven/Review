import pyautogui as pag
import time



'''
while True:
    print(pag.position())
    time.sleep(1)
'''

while True:
    dino = pag.locateOnScreen("dino.png",confidence=0.8)
    if dino:
        break

print(dino)
start = time.time()
'''
while True:
    screen = pag.screenshot()
    for i in range(310,500):
        if screen.getpixel((i,650))[0] <= 100:
            pag.keyDown('space')
            if time.time() - start <30:
                time.sleep(0.03)
            pag.keyUp('space')
            break
        if 310<i<500:
            if screen.getpixel((i,590))[0] <= 100 and screen.getpixel((i,700))[0] >= 200:
                pag.keyDown('down')
                if time.time() - start > 30:
                    time.sleep(0.35)
                elif time.time() - start >50 :           
                    time.sleep(0.22)
                pag.keyUp('down')
              
'''


'''
screen = pag.screenshot()

# print(screen.getpixel((310,1165)))

print(screen)

print(screen.getpixel((1,1)))

'''
