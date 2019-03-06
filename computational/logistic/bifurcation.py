import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')


def logistic(u, x):
    return u * x * (1-x)
#Define bifurcation plot
n = 1000
iterations = 1000
last = 100
x = 0.1 * np.ones(n)
u = np.linspace(0.0001, 4.0, n)
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(iterations):
    x = logistic(u, x)

    if i >=(iterations - last):
        ax.plot(u, x, ',k', alpha=0.25)
#Labelling
ax.minorticks_on()
ax.set_xlabel('$\mu$')
ax.set_ylabel('$x$')
ax.set_title('Bifurcation Diagram')
#Save and show
plt.savefig('./manuscript/figures/logistic/bifurcation.eps', dpi=600)

plt.show()
