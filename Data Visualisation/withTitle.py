import matplotlib.pyplot as plt
#data
x = [1, 2, 3, 4, 5]
y = [50, 65, 80, 75, 90]
y1 = [56, 65, 75, 85, 99]

plt.plot(x,y,"--",y1,":")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple 2D Plot")

plt.show()