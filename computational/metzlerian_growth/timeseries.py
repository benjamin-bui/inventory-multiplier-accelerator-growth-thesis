import numpy as np
import matplotlib.pyplot as plt


#Time series of growth with mean of last 3 prediction
def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt

#Plot timeseries
def variableplot(Variable):
    fig = plt.figure(dpi=1200)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(Variable, c='blue', linewidth=0.5)
    ax1.set_xlabel('$t$')
    ax1.set_ylabel('$\dot Y$')

#Generate time series data and plots
def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    #Simulate
    for t in range(6, iter):
        dY[t] = growth(dY[t-1], dY[t-2], dY[t-3], dY[t-5], dY[t-6], s, k, v, q,)
    variableplot(dY)
    return dY

mapping(100, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries1.eps', dpi=1200)
mapping(100, 120, 110, 100, 105, 107, 0.7, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries2.eps', dpi=1200)
mapping(29, 20 , 15 , 10, 20 ,50, 0.6, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/timeseries3.eps', dpi=1200)
mapping(100, 120, 110, 100, 105, 107, 0.3, 0.3, 500, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/chaotic_timeseries.eps', dpi=1200)
mapping(100, 120, 110, 100, 105, 107, 0.6, 0.3, 416, 0.001, 150)
plt.savefig('./manuscript/figures/metzlerian_growth/chaotic_timeseries2.eps', dpi=1200)

