import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
from tqdm import tqdm
import scipy
from scipy.fftpack import fft
#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')
def multiplier_accelerator(x, u):
    return u*x-(u+1)*x**3

def timeseries_plot(iterations, u, x0, last):
    fig = plt.figure(dpi=600)
    #Time series of mapping
    ax1 = fig.add_subplot(2, 1, 1)
    x = np.array([x0,]*iterations)
    print("Loading Time Series")
    for i in tqdm(range(iterations)):
        x[i] = multiplier_accelerator(x[i-1], u)
    #Plot time series
    ax1.plot(x, c='blue', linewidth=0.5)
    #Fourier Transform
    ax2 = fig.add_subplot(2, 1, 2)
    lastx = np.ones(last)
    for i in range(iterations):
        if i >= iterations - last:
            lastx[i-iterations] = x[i]
    fftx = fft(lastx)
    print(fftx[0])
    freq = np.linspace(0, 1, last-1)
    fftnomean = np.ones(last-1)
    for i in range(last):
        if i > 0:
            fftnomean[i-1]=fftx[i]
    ax2.plot(freq, fftnomean, c='b', linewidth=0.5)
    plt.xlim(0+1/iterations,1.0)
    print(max(fftnomean))
#Set iterations>150
timeseries_plot(400, 2.3, 0.5, 100)
plt.show()
