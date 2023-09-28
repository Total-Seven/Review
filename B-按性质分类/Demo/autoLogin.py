import pyautogui as pag
import time
import sys

COUNT = 'linjunling'
PASSWORD = '77'


'''
while True:
    print(pag.position())
    time.sleep(1)
'''

pag.moveTo(263,338,0.5) # 移动到 Edge浏览器 快捷方式上
pag.doubleClick(263,338) # 双击打开
time.sleep(0.5)
pag.hotkey('win','up') # 最大化浏览器窗口

time.sleep(1)
pag.moveTo(590,50,0.5) # 移动到地址栏
pag.click(590,50,2)

pag.press('shift') # 英文输入
pag.typewrite('jm.onlystem.com', interval=0.1) # 输入网址
pag.press('enter') # 按下`回车`键


# 移动到 账号栏  x=1128,y=355
pag.moveTo(1130,355,0.25)
pag.doubleClick(1130,355)
pag.typewrite(COUNT, interval=0.1) 

# 移动到 密码栏  x=1132,y=396
pag.moveTo(1130,395,0.25)
pag.doubleClick(1130,395)
pag.typewrite(PASSWORD, interval=0.1)

# 移动到 验证码栏 x=1130,y=450
pag.moveTo(1130,450,0.25)
pag.doubleClick(1130,450)

sys.exit()

