import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
from tqdm import tqdm
import scipy
from scipy import fftpack


#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')
def logmap(x, u):
    return u*x*(1-x)
#Creates signal from logistic map
#Set last<=iterations 
def signalgen(iterations, u, x0, last):
    signal = np.ones(iterations)*x0
    for i in range(iterations):
        signal[i] = logmap(signal[i-1],u)
    signal = signal[iterations-last:iterations]
    return(signal)

#Fourier Transform Signal
def ftransform(signal, last):
    fft_signal = fftpack.fft(signal)
    #Create 1 sided fft and doubles amplitude for plotting
    fft_plot = 2*fft_signal[:int(np.floor(last/2)+1)]
    #Normalizes frequency from 0 to 1
    fftx = np.linspace(0, 1, last/2+1)
    #Create Plot
    fig = plt.figure(dpi=600)
    ax1 = fig.add_subplot(312)
    ax2 = fig.add_subplot(311)
    ax3 = fig.add_subplot(313)
    #Ignore 0 frequency peak
    ax1.plot(fftx[1:], abs(fft_plot[1:]), c='b', linewidth=0.5)
    ax2.plot(signal, c='b', linewidth=0.25)
    ax3.plot(fftpack.ifft(fft_signal), c='b', linewidth=0.25)
    plt.show()
    
#Final Composite Function
def filtermap(iterations, u, x0, last, cutoff, *args, **kwargs):
    signal = signalgen(iterations, u, x0, last)
    ftransform(signal, last)
    
#Chaotic
#filtermap(2000, 3.8, 0.1, 1000, 2)
#2 cycle
filtermap(11000, 3.7, 0.7, 10000, 2)
#filtermap(200, 3.55, 0.1, 50, 2)

