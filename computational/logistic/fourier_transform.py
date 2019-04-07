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
def LogisticMap(x, u):
    return u*x*(1-x)

def timeseries_plot(iterations, u, x0, last):
    fig = plt.figure(dpi=1200)
    #Time series of mapping
    ax1 = fig.add_subplot(2, 1, 1)
    x = np.array([x0,]*iterations)
    for i in tqdm(range(iterations)):
        x[i] = LogisticMap(x[i-1], u)
    #Plot time series
    #ax1.set_title('Original Signal')
    #ax1.plot(x, c='blue', linewidth=0.5)
    #Fourier Transform
    ax2 = fig.add_subplot(2, 1, 2)
    lastx = np.ones(last)
    for i in range(iterations):
        if i >= iterations - last:
            lastx[i-iterations] = x[i]
    fftx = fft(lastx)
    #Plot truncated plot
    ax1.set_title('Original Signal')
    ax1.plot(lastx, c='blue', linewidth=0.5)
    print(fftx[0])
    freq = np.linspace(0, 1, last-1)
    fftnomean = np.ones(last-1)
    for i in range(last):
        if i > 0:
            fftnomean[i-1]=fftx[i]
    ax2.set_title('Fourier Transform Pre-filter')
    ax2.plot(freq, fftnomean, c='b', linewidth=0.5)
    plt.xlim(0+1/iterations,1.0)
    #Bad prototype filter
    fig2=plt.figure(dpi=1200)
    ax1_2 = fig2.add_subplot(2,1,2)
    highfft = fftx
    for i in range(last):
        if i < int(math.floor(last*0.6)):
            highfft[i] <= fftx[i]
        else:
            highfft[i] = 0
    ax1_2.set_title('Filtered Fourier')
    ax1_2.plot(highfft, c='b', linewidth=0.5)
    signal = np.fft.ifft(highfft)
    ax2_2 = fig2.add_subplot(2, 1, 1)
    ax2_2.set_title('Filtered Signal')
    ax2_2.plot(signal, c='b', linewidth=0.5)

#Set iterations>150
timeseries_plot(500, 3.9, 0.5, 100)
plt.show()
