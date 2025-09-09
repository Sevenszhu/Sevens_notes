import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color = 'red', linewidth = 1)

# xlim代表在横坐标轴上取一段范围，ylim同理
# 本质上是从整个图像上截取一段需要的
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# xlabel函数用于描述坐标轴，可以写出横坐标轴和纵坐标轴的名称
plt.xlabel('I am x')
plt.ylabel('I am y')

# 命名一个变量名，自定义坐标轴上显示的刻度点
# 因为从本质上讲，linspace是用来生成一堆数组的
new_ticks = np.linspace(-1, 2, 5)
# 打印坐标点，用来检查的
print(new_ticks)
# 替换x轴坐标
plt.xticks(new_ticks)
# 替换y轴坐标，规定用哪些字符替换哪些
plt.yticks([-2, -1.8, -1, 1.22, 3],
            ['really bad', 'bad', 'normal', 'good', 'really good'])

# gca = 'get current axis'
# gca 就是获取当前绘图的坐标轴对象
ax = plt.gca()
# spine 指的是坐标轴的脊梁（上下左右四条边框），是一个字典，键为'top' 'bottom' 'left' 'right'
# set_color('none') 其实就是隐藏边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# set_ticks_position()作用是让坐标轴显示
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# data代表根据数据坐标定位
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
