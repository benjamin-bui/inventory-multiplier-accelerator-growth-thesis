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
    ax1.set_xlabel('$t$')
    ax1.set_ylabel('$\dot Y$')

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
    for t in tqdm(range(6, iter)):
        dI[t] = invest(dY[t-1], dY[t-2], v, q)
        dC[t] = consume(dY[t-1], dY[t-2], s)
        dU[t] = predict(dC[t-1], dC[t-2], dC[t-3])
        dQ[t] = invent(dU[t], dC[t], k)
        dS[t] = pinvent(dU[t], dQ[t-1], k)
        dY[t] = growth(dU[t], dI[t], dS[t])
    variableplot(dY)

mapping(100, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries1.eps', dpi=1200)
mapping(100, 120, 110, 100, 105, 107, 0.7, 0.3, 500, 0.001, 200)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries2.eps', dpi=1200)
mapping(29, 20 , 15 , 10, 20 ,50, 0.6, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries3.eps', dpi=1200)
