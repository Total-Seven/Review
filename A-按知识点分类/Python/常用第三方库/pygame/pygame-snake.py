import pygame as pg
import random as rd
import keyboard
import sys
import time
import threading


pg.init()
sc=pg.display.set_mode((700,700))
sc.fill((0,0,0))
pos=[100,100]
color=(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
lastkey=4

def control():
    global lastkey
    keys = pg.key.get_pressed()
    speed=5
    if keys[pg.K_w]==1 or lastkey==1:
        pos[1]-=speed
        lastkey=1
    if keys[pg.K_s]==1 or lastkey==2:
        pos[1]+=speed
        lastkey=2
                              
    if keys[pg.K_a]==1 or lastkey==3:
        pos[0]-=speed
        lastkey=3
    if keys[pg.K_d]==1 or lastkey==4:
        pos[0]+=speed
        lastkey=4

                              
clock=pg.time.Clock()



def changecolor():
    timer()
    print("change")
    global color
    color = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))

def timer():
    t = threading.Timer(0.5,changecolor)
    t.start()

timer()

    
while True:
    clock.tick(60)           # 帧率60
    
    event = pg.event.poll()  # 捕捉当前的发生的事件
    if event.type == pg.QUIT:  # 退出
        pg.quit()
        exit()

    
    
    pg.draw.circle(sc,color,pos,5,0) # 在坐标pos上画一个圆⚪，颜色为color，半径radius为5，宽度为0
    control() # 控制移动
    
    pg.display.update()      # 更新画面
    
