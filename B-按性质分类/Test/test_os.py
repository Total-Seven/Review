''' 

★★★ system
    : ① 每一条system函数都会创建一个子进程在系统上执行命令行,子进程的执行结果无法影响主进程。
      ② 值是子进程运行结束后返回的状态码,
        0:成功,1:失败.256:没有返回结果.
      ③ 该方法适用于系统命令不需要输出内容的场景。

from os import system
a = system("ping 192.168.1.101")  #使用a接收返回值
print(a)


    缺点：
        如果想在获取在cmd输出的内容,是无法获取的。
        不会在错误时停止运行。
        容易被恶意注入。
'''


''' 

★★★ popon
'''
import os
a=os.popen("ping 192.168.1.101")
print(a.read())