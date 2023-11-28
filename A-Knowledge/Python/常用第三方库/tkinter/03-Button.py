import tkinter as tk
win = tk.Tk()  # 主窗体


def my_quit():
    win.quit()
    win.destroy()


but_quit = tk.Button(win, text='退出', command=my_quit, width=10, height=2)
but_quit.pack()

win.mainloop()
