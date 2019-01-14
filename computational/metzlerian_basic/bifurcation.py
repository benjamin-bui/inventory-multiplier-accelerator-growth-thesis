import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import time
from tqdm import tqdm
import statistics

#LaTeX Font
rc('text', usetex=True)
rc('font', family='serif')

#Define Function
def metzlerian(k, U, Ulag, Clag, Ibar):
    return U + k * U - (1 + k) * Ulag + Clag + Ibar
#Solves for steady state income
def ssincome(b, Ibar):
    return ( 1/(1-b) ) * Ibar
#Solves for steady state consumption
def ssconsumption(b, Ybar):
    return b * Ybar 
#Solves for U, goods produced for sale
def saledist(c, f, d, Cbar, Clag):
    Uextrapolate = Clag + c * (Clag - Cbar)
    Uregression = Clag + f * (Cbar - Clag)
    w = 1 / (1 + d * (Cbar - Clag)**2)
    return w * Uextrapolate + (1 - w)*Uregression
#Solves for consumption
def consumption(b, Ylag):
    return b * Ylag
#Solves for S, goods produced for stock
def stock(k, Ulag, Clag, U):
    qhatlag = k * Ulag
    Qlag = Qhatlag - (Clag - Ulag)
    Qhat = k * U
    return Qhat - Qlag
#Solves for timeseries data 
def timeseries(b, c, d, f, k, Y0, U0, Ibar, iterations):
    Ybar = ssincome(b, Ibar)
    Cbar = ssconsumption(b, Ybar)
    Income = np.array([Y0,]*iterations)
    Sale = np.array([U0,]*iterations)
    Consumption = np.ones(iterations)
    Stock = np.ones(iterations)
    for i in range(1, iterations):
        Consumption[i-1] = consumption(b, Income[i-1])
        Sale[i] = saledist(c, f, d, Cbar, Consumption[i-1])
        Income[i] = metzlerian(k, Sale[i], Sale[i-1], Consumption[i-1], Ibar)
    return Income

#Faster Bifurcation Diagram varying mpc, b
def bbifurcation(lower, upper, points, c, d, f, k, Y0, U0, Ibar):
    #Plot set up
    last = 10
    iterations = 1000
    fig = plt.figure(dpi=600)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    b = np.linspace(lower, upper, points)
    #Solve for each parameter value
    for j in tqdm(range(points)):
        Income = timeseries(b[j], c, d, f, k, Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                ax.plot(b[j], Income[m], ',k', alpha=0.25)
    plt.show()
bbifurcation(0.7, 0.8, 500, 0.3, 1.0, 0.5, 1 , 40.5, 30.0, 10)
