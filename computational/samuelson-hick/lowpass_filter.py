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
def multiplier_accelerator(x, u):
    return u*x-(u+1)*x**3

#Creates signal from multiplier-accelerator
#Set last<=iterations 
def signalgen(iterations, u, x0, last):
    signal = np.ones(iterations)*x0
    for i in tqdm(range(iterations)):
        signal[i] = multiplier_accelerator(signal[i-1], u)
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
    fig = plt.figure(dpi=1200)
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(211)
    #ax3 = fig.add_subplot(313)
    #Ignore 0 frequency peak
    ax1.plot(fftx[1:], abs(fft_plot[1:]), c='b', linewidth=0.5)
    ax2.plot(signal, c='b', linewidth=0.25)
    #ax3.plot(fftpack.ifft(fft_signal), c='b', linewidth=0.25)
    plt.show()
    
#Final Composite Function
def filtermap(iterations, u, x0, last, cutoff, *args, **kwargs):
    signal = signalgen(iterations, u, x0, last)
    ftransform(signal, last)
    
#Chaotic
#filtermap(2000, 3.8, 0.1, 1000, 2)
#2 cycle
filtermap(1000, 2.3, 0.1, 900, 2)
#filtermap(200, 3.55, 0.1, 50, 2)

