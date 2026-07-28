import matplotlib.pyplot as plt
#data
x = [1, 2, 3, 4, 5]
y = [50, 65, 80, 75, 90]

plt.figure(figsize=(8,4)) #always in inches

plt.plot(x,y,"--")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple 2D Plot")

plt.show()