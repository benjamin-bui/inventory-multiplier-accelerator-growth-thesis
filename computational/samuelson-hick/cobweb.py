import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
from tqdm import tqdm

#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

#Create function for cobweb plot with arguments: function, parameter, and initial value
def plot_cobweb(f, u, x0, nmax=250 ):
    x = np.linspace(-1,1,2000)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #Plot map
    ax.plot(x, f(x, u), c='black', lw=1)
    #Plot 45 degree line
    ax.plot(x, x, c='gray', lw=1, dashes=[6,2])

    #Iterate function for nmax stpdf
    px, py = np.empty((2, nmax+1, 2))
    px[0], py[0] = x0, x0
    for n in tqdm(range(1, nmax, 2)):
        px[n] = px[n-1]
        py[n] = f(px[n-1], u)
        px[n+1] = py[n]
        py[n+1] = py[n]

    #Plot path
    ax.plot(px, py, c='blue', linewidth=0.5)

    #Beautify Plot
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel('$\dot Y_t$')
    ax.axhline(0, color='k', lw=.5, alpha=0.25)
    ax.axvline(0, color='k', lw=.5, alpha=0.25)
    ax.set_ylabel('$\dot Y_{t+1}$')

class AnnotatedFunction:
    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

#Logistic Function
func = AnnotatedFunction(lambda x, u: u*x-(u+1)*x**3, r'$\mu Z-(\mu+1)Z^3$')
plot_cobweb(func, 1.5, 0.1)
plt.savefig('./manuscript/figures/sam_hicks/fixed.eps', dpi=1500)
plot_cobweb(func, 2.15, 0.1)
plt.savefig('./manuscript/figures/sam_hicks/2-cyclic.eps', dpi=1500)
plot_cobweb(func, 2.4, 0.1)
plt.savefig('./manuscript/figures/sam_hicks/chaos_contained.eps', dpi=1500)
plot_cobweb(func, 2.6, 0.1)
plt.savefig('./manuscript/figures/sam_hicks/chaos_uncontained.eps', dpi=1500)
plot_cobweb(func, 2.7, 0.1)
plt.savefig('./manuscript/figures/sam_hicks/unbound_cyclic.eps', dpi=1500)

