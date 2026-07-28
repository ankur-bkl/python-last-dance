import matplotlib.pyplot as plt
#data
x = [1, 2, 3, 4, 5]
y1 = [50, 65, 80, 75, 90]
y2 = [56, 65, 75, 85, 99]

plt.plot(x,y1,"r--", label="Sales")
plt.plot(x,y2,"y:", label="Lose")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Simple 2D Plot")

plt.legend()

plt.show()