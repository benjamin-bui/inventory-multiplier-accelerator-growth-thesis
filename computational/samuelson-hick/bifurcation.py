import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
from sympy import *
import statistics
#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

def sam_hick(u, x):
    return u*x-(u+1)*x**3
#Define bifurcation plot
def bifur_2way(n, iterations, x0, u_lower, u_upper):
    last = 50
    x = x0 * np.ones(n)
    u = np.linspace(u_lower, u_upper, n)
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    for i in range(iterations):
        x = sam_hick(u, x)
        if i >=(iterations - last):
            ax.plot(u, x, ',k', alpha=0.25)
    y = -x0 * np.ones(n)
    for i in range(iterations):
        y = sam_hick(u, y)
        if i >=(iterations-last):
            ax.plot(u, y, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\mu$')
    ax.set_ylabel('$Z$')
    ax.set_title('Bifurcation Diagram')
    ax.set_xlim(u_lower, u_upper)
bifur_2way(5000, 10000, 0.1, 0.9, 3.0)
#Save and show
plt.savefig("./manuscript/figures/sam_hicks/bifurcation.pdf", dpi=1000)

plt.show()