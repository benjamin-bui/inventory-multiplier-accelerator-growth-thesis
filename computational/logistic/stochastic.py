import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import random
import statistics
from tqdm import tqdm

#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

#Define logistic mapping
def logmap(x, u):
    return u*x*(1-x)

def gensignal(iterations, ulow, uhigh):
    #Randomly generate x0
    x0 = np.random.uniform(0, 1)
    signal = np.ones(iterations)*x0
    #Generate random parameters
    parameter = np.ones(iterations)
    for i in range(iterations):
        parameter[i] = parameter[i]*np.random.uniform(ulow, uhigh)
    #Generate signal
    for i in range(iterations):
        signal[i] = logmap(signal[i-1], parameter[i-1])

    print('Initial Value')
    print(x0)
    """
    #Generate plot
    fig = plt.figure(dpi=1200)
    ax1 = fig.add_subplot(111)
    ax1.plot(signal, c='b', linewidth='0.5')
    plt.show()
    """
gensignal(100, 1, 3)