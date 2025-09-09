import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y1 = 2 * x ** 3 
y2 = 3 * x

# figure函数相当于创建画布，默认是1234排列下去
plt.figure()
plt.plot(x, y1)

# figure函数的括号里面可以加入参数，譬如num代表序号，figsize代表画布大小
plt.figure(num = 3)
# plot是代表把散点连线，默认连线是蓝色
plt.plot(x, y2)
# plot函数后面也可以加参数，譬如颜色，宽度，线的类型
plt.plot(x, y1, color = 'red', linewidth = 1, linestyle = '--')

plt.show()
