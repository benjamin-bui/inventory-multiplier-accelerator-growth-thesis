import numpy as np
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.linalg import sqrtm

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
def partial1(dYt1, s, k, v, q):
    return ((1)/(v * (q+((dYt1**4)/v**4)))) - ((4*dYt1**4)/(v**5*(q+((dYt1**4)/v**4))))
def partial2(dYt2, s, k, v, q):
    return 1 + ((k+1)*(1-s))/3 - s + (4*dYt2**4)/(v**5*(q+((dYt2**4/v**4))) - (1)/(v*(q+((dYt2**4/v**4)))))
def lyapunov(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    dY = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter)
    Lyapunov1 = 0
    for i in range(2, iter):
        Lyapunov1 += np.log(partial1(dY[i-1], s, k, v, q))
    lyexp1 = Lyapunov1 / (iter-2)
    return lyexp1
def lyapunov2(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    dY = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter)
    Lyapunov2 = 0
    for i in range(2, iter):
        Lyapunov2 += np.log(partial2(dY[i-2], s, k, v, q))
    lyexp2 = Lyapunov2 / (iter-2)
    return lyexp2
def testlyplot(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, k, v, q, iter):
    #Plot set up
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    s = np.linspace(lower, upper, points)
    xaxis = s
    yaxis2 = np.ones(points)
    for i in tqdm(range(points)):
        yaxis2[i] = lyapunov2(dY0, dY1, dY2, dY3, dY4, dY5, s[i], k, v, q, iter)
    # ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    ax.plot(xaxis, yaxis2, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$s$')
    ax.set_ylabel('$\lambda$')

testlyplot(0.0, 1.0, 10000, 100, 120, 110, 100, 105, 107, 0.3, 500, 0.001, 1000)
plt.savefig('./manuscript/figures/metzlerian_growth/naivelyapunov.eps', dpi=1200)
