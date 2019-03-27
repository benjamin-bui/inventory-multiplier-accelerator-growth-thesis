import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Time series with mean of last 3 prediction
def growth(dUt, dIt, dSt):
    dYt = dUt + dIt + dSt
    return dYt
def invest(dYt1, dYt2, v, q):
    dIt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q)
    return dIt
def consume(dYt1, dYt2, s):
    dCt = (1 - s) * dYt1 + s * dYt2
    return dCt
def predict(dCt1, dCt2, dCt3):
    dUt = (dCt1 + dCt2 + dCt3) / 3
    return dUt
def invent(dUt, dCt, k):
    dQt = (k + 1) * dUt - dCt
    return dQt
def pinvent(dUt, dQt1, k):
    dSt = k * dUt - dQt1
    return dSt

#Plot timeseries
def variableplot(Variable):
    fig = plt.figure(dpi=600)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(Variable, c='blue', linewidth=0.5)

def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):

    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    dI = np.zeros(iter)
    dC = np.zeros(iter)
    dU = np.zeros(iter)
    dQ = np.zeros(iter)
    dS = np.zeros(iter)
    for t in range(2, 6):
        dI[t] = invest(dY[t-1], dY[t-2], v, q)
        dC[t] = consume(dY[t-1], dY[t-2], s)
    for t in range(5, 6):
        dU[t] = predict(dC[t-1], dC[t-2], dC[t-3])
        dQ[t] = invent(dU[t], dC[t], k)
    #Simulate
    for t in range(6, iter):
        dI[t] = invest(dY[t-1], dY[t-2], v, q)
        dC[t] = consume(dY[t-1], dY[t-2], s)
        dU[t] = predict(dC[t-1], dC[t-2], dC[t-3])
        dQ[t] = invent(dU[t], dC[t], k)
        dS[t] = pinvent(dU[t], dQ[t-1], k)
        dY[t] = growth(dU[t], dI[t], dS[t])
    return dY

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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
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
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$\dot Y_5$')
    ax.set_ylabel('$\dot Y$')

y0bifurcation(-400, 400, 5000, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y0bifurcation.eps', dpi=1200)
y1bifurcation(-400, 400, 5000, 100, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y1bifurcation.eps', dpi=1200)
y2bifurcation(-400, 400, 5000, 100, 120, 100, 105, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y2bifurcation.eps', dpi=1200)
y3bifurcation(-400, 400, 5000, 100, 120, 110, 105, 107, 0.6, 0.3, 500, 0.001,)
plt.savefig('./manuscript/figures/metzlerian_growth/y3bifurcation.eps', dpi=1200)
y4bifurcation(-400, 400, 5000, 100, 120, 110, 100, 107, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y4bifurcation.eps', dpi=1200)
y5bifurcation(-400, 400, 5000, 100, 120, 110, 100, 105, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/y5bifurcation.eps', dpi=1200)