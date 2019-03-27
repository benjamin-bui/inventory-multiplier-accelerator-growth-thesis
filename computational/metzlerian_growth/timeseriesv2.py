import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
#Time series with mean of last 3 prediction
def growth(dY1, dY2, dY3, dY5, dY6, s, k, v, q):
    dYt = (dY1 / v) / ( (dY1 / v)**4 + q) - (dY2 / v) / ( (dY2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dY2-dY5)+s*(dY3-dY6)) + (1-s)*dY2 + s*dY3
    return dYt

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
    #Simulate
    for t in tqdm(range(6, iter)):
        dY[t] = growth(dY0, dY1, dY2, dY3, dY5, s, k, v, q,)
    variableplot(dY)

mapping(100, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseriestest.eps', dpi=1200)

