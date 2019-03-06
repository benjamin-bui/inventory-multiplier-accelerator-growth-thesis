import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

#Create function for cobweb plot with arguments: function, parameter, and initial value
def plot_cobweb(f, u, x0, nmax=1000):
    x = np.linspace(0,1,1000)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #Plot map
    ax.plot(x, f(x, u), c='black', lw=0.2)
    #Plot 45 degree line
    ax.plot(x, x, c='gray', lw=1, dashes=[6,2])

    #Iterate function for nmax steps
    px, py = np.empty((2, nmax+1, 2))
    px[0], py[0] = x0, x0
    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1], u)
        px[n+1] = py[n]
        py[n+1] = py[n]

    #Plot path
    ax.plot(px, py, c='blue')

    #Beautify Plot
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.axhline(0, color='k', lw=.5, alpha=0.25)
    ax.axvline(0, color='k', lw=.5, alpha=0.25)
    ax.set_aspect('equal')
    ax.set_xlabel('$x$')
    ax.set_ylabel(f.latex_label)
    ax.set_title('$x_0 = {:1}, \mu = {:2}$'.format(x0, u))

class AnnotatedFunction:
    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

#Logistic Function
func = AnnotatedFunction(lambda x, u: u*x*(1-x), r'$\mu x_t(1-x_t)$')
plot_cobweb(func, 1.5, 0.1)
plt.savefig('./manuscript/figures/logistic/fixed_cob.eps', dpi=600)
plot_cobweb(func, 3.2, 0.799455)
plt.savefig('./manuscript/figures/logistic/2-cyclic_cob.eps', dpi=600)
plot_cobweb(func, 3.82842712, 0.5)
plt.savefig('./manuscript/figures/logistic/3-cyclic_cob.eps', dpi=600)
plot_cobweb(func, 3.8, 0.1)
plt.savefig('./manuscript/figures/logistic/chaos_cob.eps', dpi=600)

