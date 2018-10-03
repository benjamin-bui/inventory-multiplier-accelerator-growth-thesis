from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
result = []
lambdas = []
maps = []

#Define N, higher value increases accuracy of approximation
N = 2000
umin = 1
umax = 3
uinterval = 0.01
#Define range of u
uvalues = np.arange(umin, umax, uinterval)

#Loop through u
for u in uvalues:
    x = 0.5
    result = []
    #Iterate this system N times
    for t in range(N):
        x = u*x - (u+1)*x**3
        #Calculate log of absolute derivative (Magnifies divergence)
        result.append(math.log(abs(u - 3*(1+u) * x**2)+0.00000001) )
    #Take average of results
    lambdas.append(statistics.mean(result))
    #Ignore first 100 results as parth of time path
    for t in range(20):
        x = u*x - (u+1)*x**3
        maps.append(x)

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)

xticks = np.linspace(0, 3, 4000)
# zero line
zero = [0]*4000
ax1.plot(xticks, zero, 'g-')
# plot map
ax1.plot(xticks, maps, 'r.',alpha = 0.3, label = 'Map', ls='', marker=',')
ax1.set_xlabel('u')
# plot lyapunov
ax1.plot(uvalues, lambdas, 'b-', linewidth = 3, label = 'Lyapunov exponent')
ax1.grid('True')
ax1.set_xlabel('r')
ax1.legend(loc='best')
ax1.set_title('Map of x(t+1) = x(t) + r - x(t)^2 versus Lyapunov exponent')

plt.show()
