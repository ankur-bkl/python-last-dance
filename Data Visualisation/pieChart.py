import matplotlib.pyplot as plt
#data
x = ["A","B","C","D","E"]
y = [50, 65, 80, 75, 90]
# y2 = [56, 65, 75, 85, 99]

plt.pie(y,labels=y,autopct="%.1f%%")
plt.title("Pie Chart")

plt.show()