import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
from tqdm import tqdm
import scipy

def output(it, st, ut):
    yt = it + st + ut
    return yt

def invent(ut, ut1, ct1, k):
    qthat = k * ut
    qthat1 = k * ut1
    qt1 = qthat1 - (ct1 - ut1)
    st = qthat - qt1
    return st

def invest(yt1, yt2, v, q):
    it = v * np.tanh((yt1-yt2) / q)
    return it

def consume(yt1, yt2, s):
    ct = (1 - s) * yt1 + s * yt2
    return ct 

def predict(ct1, ct2, eta1):
    ut = ct1 + eta1 * (ct1 - ct2)
    return ut

def adapt(ct1, ct2, ct3):
    if (ct1 - ct2) == (ct2 - ct3):
        eta1 = 0
    else:
        eta1 = (ct1 - ct2) / (ct2 - ct3)
    return eta1

#Plot timeseries
def income_plot(Income):
    fig = plt.figure(dpi=600)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(Income, c='blue', linewidth=0.5)
    plt.show()

def timeseries(y0, y1, y2, y3, c0, c1, i0, i1, eta0, s, v, q, k, iter):
    """
    Vectors are initialized given initial values given to function.
    Income is initialized with initial t=[0,1,2,3]  
    Consumption and Investment are calculated 2 period lag of Income so initial values must be given for t=[0,1]. 
    Starting vector for Consumption and Income also includes calculated values for t=[2,3,4] based on income. 
    Starting vector for Inventory is initialized with t=[0,1,2,3] based on Income - Consumption - Investment
    Starting vector for Predicted income is initialized with values based on Consumption and Adaptive predictive parameter for t=[1,2,3,4].
    Starting vector for adaptive parameter is initialized with constant 
    """

    #Set up income vector
    Income = np.append([y0, y1, y2, y3], np.ones(iter-4))
    #Set up consumption vector
    Consumption = np.append([c0, c1, consume(y1, y0, s), consume(y2, y1, s)],[np.ones(iter-4)])
    #Set up investment vector, given 2 initial values 
    Investment = np.append([i0, i1, invest(y1, y0, v, q), invest(y2, y1, v, q)],[np.ones(iter-4)])
    #Set up adaptive expectation coefficient vector, set as constant for first 3 time periods
    Adaptive = np.append([eta0, eta0, eta0], np.ones(iter-3))
    #Set up predicted income vector
    Predicted = np.ones(iter)
    Predicted[2] = predict(Consumption[1], Consumption[0], Adaptive[1])
    Predicted[3] = predict(Consumption[2], Consumption[1], Adaptive[2])
    #Set up inventory vector based on determined income, consumption, and investment
    Inventory_purchase = np.ones(iter)
    for i in range(4):
        Inventory_purchase[i] = Income[i] - Consumption[i] - Investment[i]
    """
    Simulates behavior of the expanded Metzlerian model for "iter" time periods
    """
    for i in tqdm(range(4, iter)):
        Consumption[i] = consume(Income[i-1], Income[i-2], s)
        Investment[i] = invest(Income[i-1], Income[i-2], v, q)
        Adaptive[i-1] = adapt(Consumption[i-1], Consumption[i-2], Consumption[i-3])
        Predicted[i] = predict(Consumption[i-1], Consumption[i-2], Adaptive[i-1])
        Inventory_purchase[i] = invent(Predicted[i], Predicted[i-1], Consumption[i-1], k)
        Income[i] = output(Investment[i], Inventory_purchase[i], Predicted[i])
    income_plot(Income)
    print(Income)

#Apply function mapping
#Function arguments in order: y0, y1, y2, y3, c0, c1, i0, i1, eta0, s, v, q, k, iter
timeseries(100, 120, 130, 140, 60, 70, 40, 67, 4.0, 0.3, 50, 100, 0.2, 50)
