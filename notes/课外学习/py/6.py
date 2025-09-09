import matplotlib.pyplot as plt
import numpy as np 

x = np.linespace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num = 1, figsize = (8, 5),)
plt.plot(x, y, )

ax = plt.gca()
ax.spines['right
