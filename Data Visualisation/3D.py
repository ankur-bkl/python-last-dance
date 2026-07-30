from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

fig =plt.figure() # empty canvas

ax =fig.add_subplot(111,projection="3d")

x = [1,2,3]

y = [4,5,6]

z = [7,8,9]

ax.plot(x,y,z) #Plots the points and joins them with a line.

plt.show()