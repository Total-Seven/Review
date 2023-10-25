import tkinter as tk
import tkinter.messagebox
win = tk.Tk()
win.title("登录界面")
win.geometry("250x130")

""" 设置变量 """
var_Name = tk.StringVar()
var_Name.set("")
var_Pwd = tk.StringVar()
var_Pwd.set("")

""" 按键处理 """


def login():
    tk.messagebox.showinfo(title="用户登录", message="成功!") if var_Name.get() == 'admin' and var_Pwd.get(
    ) == "python" else tk.messagebox.showinfo(title="用户登录", message="失败!")


def cancel():
    var_Name.set('')
    var_Pwd.set('')


def _quit():
    win.quit()
    win.destroy()


""" 组件设计 """
# 提示标签
labname = tk.Label(win, text="账号:", width=80)
labpwd = tk.Label(win, text="密码:", width=80)
# 输入框
entname = tk.Entry(win, width=100, textvariable=var_Name)
entpwd = tk.Entry(win, show="*", width=100, textvariable=var_Pwd)
# 按钮
but_Ok = tk.Button(win, text='登录', command=login)
but_Cancel = tk.Button(win, text="重置", command=cancel)
but_quit = tk.Button(win, text='退出', command=_quit)

""" 布局定位 """
labname.place(x=20, y=10, width=80, height=20)
labpwd.place(x=20, y=40, width=80, height=20)
entname.place(x=120, y=10, width=80, height=20)
entpwd.place(x=120, y=40, width=80, height=20)
but_Ok.place(x=30, y=80, width=50, height=20)
but_Cancel.place(x=100, y=80, width=50, height=20)
but_quit.place(x=170, y=80, width=50, height=20)

""" 结束 """
win.mainloop()
