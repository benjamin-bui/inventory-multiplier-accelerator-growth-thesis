import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib import rc

# Plot derivative of mapping with respect to time lag periods

def ddYt1(lower, upper, points, s, k, v, q):
    xaxis = np.linspace(lower, upper, points)
    yaxis = np.ones(points)
    for i in range(points):
        yaxis[i] = -( ( 4*xaxis[i]**4 ) / ( v**5 * ( q + ( ( xaxis[i]**4 ) / v**4 ) )**2 ) ) + ( 1 / (v * (q + ( ( xaxis[i]**4 ) / v**4 ) ) ) )
    fig = plt.figure(dpi=1200)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xaxis, yaxis, c='blue', linewidth=0.5)
    ax1.set_xlabel('$Y_{t-1}}$')
    ax1.set_ylabel('$\partial f/\partial Y_{t-1}$')        
    
def ddYt2(lower, upper, points, s, k, v, q):
    xaxis = np.linspace(lower, upper, points)
    yaxis = np.ones(points)
    for i in range(points):
        yaxis[i] = 1 + ( ( k + 1 ) * ( 1 - s ) ) / 3 - s + ( 4*xaxis[i]**4 ) /  ( v**5 * ( q + ( ( xaxis[i]**4 / v**4 ) ) )**2 ) - 1 / ( v * ( q + (xaxis[i]**4 / v**4 )))
    fig = plt.figure(dpi=1200)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xaxis, yaxis, c='blue', linewidth=0.5)
    ax1.set_xlabel('$A_{t-1}$')
    ax1.set_ylabel('$\partial f/\partial A_{t-1}$')   

ddYt1(-300.0, 300.0, 10000, 0.6, 0.3, 500.0, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/derivative1.eps', dpi=1200)
ddYt2(-300, 300, 10000, 0.6, 0.3, 500, 0.001)
plt.savefig('./manuscript/figures/metzlerian_growth/derivative2.eps', dpi=1200)