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
    Qhatlag = k * Ulag
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
    for i in range(1, iterations):
        Consumption[i-1] = consumption(b, Income[i-1])
        Sale[i] = saledist(c, f, d, Cbar, Consumption[i-1])
        Income[i] = metzlerian(k, Sale[i], Sale[i-1], Consumption[i-1], Ibar)
    return Income

#Bifurcation Diagram varying mpc, b
def bbifurcation(lower, upper, points, c, d, f, k, Y0, U0, Ibar):
    #Plot set up
    last = 50
    iterations = 1000
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    b = np.linspace(lower, upper, points)
    xaxis = np.repeat(b, last)
    yaxis = []
    #Solve for each parameter value
    print("b Bifurcation")
    for j in tqdm(range(points)):
        Income = timeseries(b[j], c, d, f, k, Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$b$')
    ax.set_ylabel('$Y$')
    
    #Save and show
    plt.savefig('./manuscript/figures/metzlerian_basic/bbifurcation.eps', dpi=1500)
#Bifurcation Diagram varying expected deviation from equilibrium, c
def cbifurcation(lower, upper, points, b, d, f, k, Y0, U0, Ibar):
    #Plot set up
    last = 50
    iterations = 1000
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    c = np.linspace(lower, upper, points)
    xaxis = np.repeat(c, last)
    yaxis = []
    #Solve for each parameter value
    print("c Bifurcation")
    for j in tqdm(range(points)):
        Income = timeseries(b, c[j], d, f, k, Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$c$')
    ax.set_ylabel('$Y$')
    
    #Save and show
    plt.savefig('./manuscript/figures/metzlerian_basic/cbifurcation.eps', dpi=1500)
#Bifurcation Diagram varying desired level of consumption relative to expected sale of consumption goods, k
def kbifurcation(lower, upper, points, b, c, d, f, Y0, U0, Ibar):
    #Plot set up
    last = 50
    iterations = 1000
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    k = np.linspace(lower, upper, points)
    xaxis = np.repeat(k, last)
    yaxis = []
    #Solve for each parameter value
    print("k Bifurcation")
    for j in tqdm(range(points)):
        Income = timeseries(b, c, d, f, k[j], Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$k$')
    ax.set_ylabel('$Y$')
    
    #Save and show
    plt.savefig('./manuscript/figures/metzlerian_basic/kbifurcation.eps', dpi=1500)

#Bifurcation Diagram varying popularity of regressive expectations, d
def dbifurcation(lower, upper, points, b, c, f, k, Y0, U0, Ibar):
    #Plot set up
    last = 50
    iterations = 1000
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    d = np.linspace(lower, upper, points)
    xaxis = np.repeat(d, last)
    yaxis = []
    #Solve for each parameter value
    print("d Bifurcation")
    for j in tqdm(range(points)):
        Income = timeseries(b, c, d[j], f, k, Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$d$')
    ax.set_ylabel('$Y$')
    
    #Save and show
    plt.savefig('./manuscript/figures/metzlerian_basic/dbifurcation.eps', dpi=1500)

#Improved efficiency bifurcation diagram varying f
def fbifurcation(lower, upper, points, b, c, d, k, Y0, U0, Ibar):
    #Plot set up
    last = 50
    iterations = 1000
    fig = plt.figure(dpi=1000)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    f = np.linspace(lower, upper, points)
    xaxis = np.repeat(f, last)
    yaxis = []
    #Solve for each parameter value
    print("f Bifurcation")
    for j in tqdm(range(points)):
        Income = timeseries(b, c, d, f[j], k, Y0, U0, Ibar, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$f$')
    ax.set_ylabel('$Y$')
    
    #Save and show
    plt.savefig('./manuscript/figures/metzlerian_basic/fbifurcation.eps', dpi=1500)

bbifurcation(0.6, 0.85, 10000, 0.3, 1.0, 0.1, 0.1, 40.6, 30.5, 10)
cbifurcation(0.1, 0.9, 10000, 0.75, 1.0, 0.1, 0.1, 40.5, 30.5, 10)
kbifurcation(0.1, 0.4, 10000, 0.75, 0.3, 0.1, 0.1, 40.5, 30.5, 10)
dbifurcation(0.01, 2.0, 10000, 0.75, 0.3, 0.1, 0.1, 40.5, 30.5, 10)
fbifurcation(0.1, 0.5, 10000, 0.75, 0.3, 1.0, 0.1, 40.0, 30.5, 10)

