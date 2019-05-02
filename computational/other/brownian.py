import numpy as np 
import matplotlib.pyplot as plt

def timeseries(mean, sigma, iterations):
    #Time series of mapping
    fig = plt.figure(dpi=1200)
    ax1 = fig.add_subplot(1, 1, 1)
    for j in range(10):
        position = sigma * np.random.randn(iterations, 1) + mean
        position[0] = 0
        for i in range(1, iterations):
            position[i] = position[i-1] + position[i]
        ax1.plot(position, c='blue', linewidth=0.5)
    plt.ylabel('y(t)')
    plt.xlabel('t')
timeseries(0, 1, 100)
plt.savefig('./presentation-2/figures/brownian_motion.eps', dpi=1200)
    