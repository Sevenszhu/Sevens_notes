import matplotlib.pyplot as plt
import numpy as np

# linspace 是numpy的一个函数，使得变量生成一个数组
# python中，变量不需要提前定义
# 这里是为了生成绘图的横坐标
# -1 到1是范围，50代表在这个范围内分隔50个点，可以使得曲线更加平滑
x = np.linspace(-1, 1, 50)
y = 2 * x ** 2 + 1
# plot用于将两组数据对应的点连接起来 
plt.plot(x, y)
# 显示已经绘制好的图像
plt.show()
