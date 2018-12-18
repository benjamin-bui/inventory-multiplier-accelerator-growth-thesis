import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

def logistic(r, x):
    return u * x * (1-x)

#Range of u values and interval between each
n = 160000
u = np.linspace(0.0001, 4.0, n)

#Higher iteration count increases approxmation accuracy
iterations = 50000
#Set initial value
x0 = 0.1 
x = 0.1 * np.ones(n)

#Lyapunov calculation
lyapunov = np.zeros(n)
fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(iterations):
    x = logistic(u, x)
    #Compute partial sums using log of absolute value of derivative
    lyapunov += np.log(abs(u * (1 - 2 * x)))

#Plotting Lyapunov
ax.plot(u[lyapunov < 0],
         lyapunov[lyapunov < 0] / iterations,
         '.k', alpha=.5, ms=.5)
ax.plot(u[lyapunov >= 0],
        lyapunov[lyapunov >= 0] / iterations,
        '.r', alpha=.5, ms=.5)
#Labelling
ax.minorticks_on()
ax.set_xlabel('$\mu$')
ax.set_ylabel('$\lambda$')
ax.set_title('Lyapunov Plot')
ax.set_ylim(-2, 1)
ax.axhline(0, color='k', lw=.5, alpha=.5)
#Save and show
plt.savefig('./manuscript/figures/logistic/lyapunov.pdf', dpi=600)
plt.show()



