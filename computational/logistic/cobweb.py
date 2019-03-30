import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

#Define Function
def logistic(u, x):
    return u * x * (1-x)
#Plots cobweb plot
def cobweb(u, X0, iterations):
    px, py = np.empty((2, iterations+1, 2))
    px[0], py[0] = X0, X0
    for i in range(1, iterations, 2):
        px[i] = px[i-1]
        py[i] = logistic(u, px[i-1])
        px[i+1] = py[i]
        py[i+1] = py[i]

    x = np.linspace(0,50,1000)
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    ax.plot(x, x, c='gray', lw=1, dashes=[6,2])
    ax.plot(px, py, c='blue', linewidth=0.5)
    #Beautify Plot
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.axhline(0, color='k', lw=.5, alpha=0.25)
    ax.axvline(0, color='k', lw=.5, alpha=0.25)
    ax.set_aspect('equal')
    ax.set_xlabel('$X_t$')
    ax.set_ylabel('$X_{t+1}$')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
cobweb(1.5, 0.1, 1000)
plt.savefig('./manuscript/figures/logistic/fixed_cob.eps', dpi=600)
cobweb(3.2, 0.799455, 1000)
plt.savefig('./manuscript/figures/logistic/2-cyclic_cob.eps', dpi=600)
cobweb(3.82842712, 0.5, 1000)
plt.savefig('./manuscript/figures/logistic/3-cyclic_cob.eps', dpi=600)
cobweb(3.8, 0.1, 1000)
plt.savefig('./manuscript/figures/logistic/chaos_cob.eps', dpi=600)
