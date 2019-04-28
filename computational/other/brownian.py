import numpy as np 
import matplotlib.pyplot as plt

def timeseries(mean, sigma, iterations):
    position = sigma * np.random.randn(iterations, 1) + mean
    for i in range(iterations):
        position[i] = position[i-1] + position[i]
    #Time series of mapping
    fig = plt.figure(dpi=1200)
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(position, c='blue', linewidth=0.5)
    plt.ylabel('y(t)')
    plt.xlabel('t')
timeseries(0, 1, 100)
plt.savefig('./presentation-2/figures/brownian_motion.eps', dpi=1200)
    