import matplotlib.pyplot as plt
import numpy as np

plt.rc('font',family='FangSong')

fig, ax = plt.subplots(figsize=(12,8))

size = 0.3
#vals = np.array([[60., 32.], [37., 40.], [29., 10.],[29., 10.]])

vals = np.array([[20., 20., 20., 20., 20.],
                 [25., 25., 25., 25., 0],
                 [29., 10., 14., 0, 0],
                 [29., 10., 0, 0, 0]])

# 颜色
colorset = plt.colormaps["Pastel1"]
outer_colors = colorset([0, 2, 4, 6])
inner_colors = colorset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3])


# outer_pie = ax.pie(dataset.sum(axis=1), radius=1, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'), labels=['Category A', 'Category B', 'Category C'])

# inner_pie = ax.pie(dataset.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

# 饼图
outer_pie = ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'),labels=['Pyhon语法学习', '智能硬件应用掌握', 'AI技术原理探究','学科知识融合'])

inner_pie = ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'),)

ax.set(aspect="equal", title='计算机视觉(基础) 1/25')

ax.legend(outer_pie[0], ['Category A', 'Category B', 'Category C'], loc='upper left', title='Outer Categories')
ax.legend(inner_pie[0], ['if条件语句', 'for循环语句', '参数与列表', '对象调用方法', 'pingpong库的调用',
                         'nano主控板的学习与应用', '8*8WS2812点阵灯学习与应用', 'nano扩展板的学习与应用', '智能硬件的编程控制',
                         '手势识别的两种判定方法','mediapipe手部关键点识别的原理','mediapipe手部关键点识别的判定',
                         '二维坐标知识(x,y)','人工智能的构成'
                         ][:len(vals.flatten())], loc='upper right', title='内部模块')
plt.show()
