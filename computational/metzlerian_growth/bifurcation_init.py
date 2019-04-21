import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Time series with mean of last 3 prediction
def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt

#Creates mapping for growth model based on growth function
def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    #Simulate
    for t in range(6, iter):
        dY[t] = growth(dY[t-1], dY[t-2], dY[t-3], dY[t-5], dY[t-6], s, k, v, q,)
    return dY

# Solves for last 20 values of growth as a single parameter is changed
# All functions below vary a single parameter between 'lower' and 'upper'
def y0bifurcation(lower, upper, points, dY1, dY2, dY3, dY4, dY5, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y0 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y0, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_0$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(Y0[j], dY1, dY2, dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_0$')
    ax.set_ylabel('$\dot Y$')

def y1bifurcation(lower, upper, points, dY0, dY2, dY3, dY4, dY5, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y1 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y1, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_1$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, Y1[j], dY2, dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_1$')
    ax.set_ylabel('$\dot Y$')

def y2bifurcation(lower, upper, points, dY0, dY1, dY3, dY4, dY5, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y2 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y2, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_2$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, Y2[j], dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_2$')
    ax.set_ylabel('$\dot Y$')

def y3bifurcation(lower, upper, points, dY0, dY1, dY2, dY4, dY5, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y3 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y3, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_3$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, Y3[j], dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_3$')
    ax.set_ylabel('$\dot Y$')

def y4bifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY5, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y4 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y4, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_4$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, Y4[j], dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_4$')
    ax.set_ylabel('$\dot Y$')

def y5bifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, s, k, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    Y5 = np.linspace(lower, upper, points)
    xaxis = np.repeat(Y5, last)
    yaxis = []
    #Solve for each parameter value
    print("$\dot Y_5$ Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, Y5[j], s, k, v, q, iterations)
        lastvalues = Income[-last:]
        yaxis.extend(lastvalues)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_5$')
    ax.set_ylabel('$\dot Y$')

y0bifurcation(-400, 400, 10000, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y0bifurcation.eps', dpi=1200)
y1bifurcation(-400, 400, 10000, 100, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y1bifurcation.eps', dpi=1200)
y2bifurcation(-400, 400, 10000, 100, 120, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y2bifurcation.eps', dpi=1200)
y3bifurcation(-400, 400, 10000, 100, 120, 110, 105, 107, 0.6, 0.3, 500, 0.001,)
plt.savefig('./manuscript/figures/metzlerian_growth/y3bifurcation.eps', dpi=1200)
y4bifurcation(-400, 400, 10000, 100, 120, 110, 100, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y4bifurcation.eps', dpi=1200)
y5bifurcation(-400, 400, 10000, 100, 120, 110, 100, 105, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y5bifurcation.eps', dpi=1200)