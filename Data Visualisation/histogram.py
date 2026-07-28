import matplotlib.pyplot as plt

import random
data =[random.randint(1,10) for _ in range(100)]

plt.hist(data,bins=6,color="red")
plt.title("Histogram")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()