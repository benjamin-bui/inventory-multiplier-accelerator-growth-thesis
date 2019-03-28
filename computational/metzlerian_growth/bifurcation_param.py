import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Time series with mean of last 3 prediction
#Time series with mean of last 3 prediction
def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt


def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    #Simulate
    for t in range(6, iter):
        dY[t] = growth(dY[t-1], dY[t-2], dY[t-3], dY[t-5], dY[t-6], s, k, v, q,)
    return dY

def sbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, k, v, q):
    #Plot set up
    last = 30
    iterations = 2000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    s = np.linspace(lower, upper, points)
    xaxis = np.repeat(s, last)
    yaxis = []
    #Solve for each parameter value
    print("s Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s[j], k, v, q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$s$')
    ax.set_ylabel('$\dot Y$')
    #Save and show

def kbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, v, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    k = np.linspace(lower, upper, points)
    xaxis = np.repeat(k, last)
    yaxis = []
    #Solve for each parameter value
    print("k Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k[j], v, q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$k$')
    ax.set_ylabel('$\dot Y$')
    #Save and show

def qbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, v):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    q = np.linspace(lower, upper, points)
    xaxis = np.repeat(q, last)
    yaxis = []
    #Solve for each parameter value
    print("q Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q[j], iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$q$')
    ax.set_ylabel('$\dot Y$')
    #Save and show


def vbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, q):
    #Plot set up
    last = 20
    iterations = 1000
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    v = np.linspace(lower, upper, points)
    xaxis = np.repeat(v, last)
    yaxis = []
    #Solve for each parameter value
    print("v Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v[j], q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                yaxis = np.append(yaxis, Income[m])
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$v$')
    ax.set_ylabel('$\dot Y$')

sbifurcation(0.65, 0.9, 10000, 29, 30 , 50 , 100, 20, 50, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/sbifurcation.eps', dpi=1200)
kbifurcation(0.1, 0.9, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/kbifurcation.eps', dpi=1200)
kbifurcation(0.1, 0.9, 10000, 29, 30 , 50 , 100, 20, 50, 0.7, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/kbifurcation2.eps', dpi=1200)
vbifurcation(1, 2000, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 0.3, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/vbifurcation.eps', dpi=1200)
qbifurcation(0, 0.0001, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 0.3, 500)
plt.savefig('./manuscript/figures/metzlerian_growth/qbifurcation.eps', dpi=1200)
