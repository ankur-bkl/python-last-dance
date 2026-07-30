import matplotlib.pyplot as plt
import numpy as np

# t=[0,20,45,60,90]

# x=[i*(np.pi/180) for i in t] #now x has angle in radiance

# plt.plot(t,np.sin(x),marker="^",label="sins")
# plt.plot(t,np.cos(x),marker="o",label="cos")

# plt.legend()

x=np.linspace(-np.pi,np.pi,10) #np.linspace(start, stop, number_of_values)

plt.plot(x,np.sin(x),marker="^",label="sin")
plt.plot(x,np.cos(x),marker=">",label="cos")

# plt.legend()


plt.title("Sin and Cos Graph")

plt.xlabel("Angles")
plt.ylabel("Values")

plt.show()