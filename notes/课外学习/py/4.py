import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3,],
        [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# ,不能少，用于提取plot中的Line2D对象提取出来，赋值给l1 
# label, 设定默认初始标签，后面legend可重新指定
l1, = plt.plot(x, y2, label = 'up')
l2, = plt.plot(x, y1, color = 'red', linewidth = 1, linestyle = '--', label = 'down')
# legend 是自定义图例
# handle 指定哪些线条参与产生图例
# label 给图例设置最终显示的文本
# loc 选择图例的位置
plt.legend(handles = [l1, l2],  labels = ['aaa', 'bbb'],loc = 'best')


plt.show()
