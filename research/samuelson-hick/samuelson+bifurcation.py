import matplotlib.pyplot as plt
import numpy as np
#Set amount of different points of parameter and range
N=5000
P=np.linspace(0.7,4,N)
m=0.7
# Create containers for coordinates
X = []
Y = []
#Create function
for u in P:
    # Add one value to X instead of resetting it.
    X.append(u)
    # Start with random m
    m = np.random.random()
    for n in range(10):
      m=(u*m)*(u+1)*m**2
    for l in range(100):
      m=(u*m)*(u+1)*m**2
    #Append to Y
    Y.append(m)

plt.plot(X, Y, ls='', marker=',')
plt.show()
