import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
from sympy import *
#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

def sam_hick(u, x):
    return u*x-(u+1)*x**3
#Range of u values and interval between each
n = 1000000
u = np.linspace(0.0001, 3.0, n)

#Higher iteration count increases approxmation accuracy
iterations = 100000
#Set initial value
x0 = 0.1 
x = 0.1 * np.ones(n)

#Lyapunov calculation
lyapunov = np.zeros(n)
fig = plt.figure(dpi=1000)
ax = fig.add_subplot(111)

for i in range(iterations):
    x = sam_hick(u, x)
    #Compute partial sums using log of absolute value of derivative
    lyapunov += np.log(abs(u-3*(u+1)*x**2))

#Plotting Lyapunov
ax.plot(u[lyapunov < 0],
         lyapunov[lyapunov < 0] / iterations,
         ',k', alpha=.25)
ax.plot(u[lyapunov >= 0],
        lyapunov[lyapunov >= 0] / iterations,
        ',r', alpha=.25)
#Labelling
ax.minorticks_on()
ax.set_xlabel('$\mu$')
ax.set_ylabel('$\lambda$')
ax.set_title('Lyapunov Plot')
ax.set_ylim(-2, 1)
ax.axhline(0, color='k', lw=.5, alpha=0.25)
#Save and show
plt.savefig('./manuscript/figures/sam_hicks/lyapunov.pdf', dpi=1000)
plt.show()



