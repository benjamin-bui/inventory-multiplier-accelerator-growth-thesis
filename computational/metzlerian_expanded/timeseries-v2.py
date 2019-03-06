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

def inventory(qt1, st, ut, ct):
    qt = qt1 + st + (ut - ct)
    return qt

def invent_purchase(ut, qt1, k):
    st = k * ut - qt1
    return st
#Hyperbolic tangent investment
'''
def invest(yt1, yt2, v, q):
    it = v * np.tanh((yt1-yt2) / q)
    return it
'''
#Cubic investment
def invest(yt1, yt2, v, q):
    it = v * ((yt1-yt2) / q) - v * ((yt1 - yt2) / q) **3
    return it

def consume(yt1, yt2, s):
    ct = (1 - s) * yt1 + s * yt2
    return ct 

def predict(ct1, ct2, eta1):
    ut = ct1 + eta1 * (ct1 - ct2)
    return ut

def adapt(ct1, ct2, ct3):
    eta1 = (ct1 - ct2) / (ct2 - ct3)
    return eta1

#Plot timeseries
def variable_plot(Variable):
    fig = plt.figure(dpi=600)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(Variable, c='blue', linewidth=0.5)
    plt.show()

'''
Simulate the model for iter time-periods
Begins by initializing variable vectors

Initialize variable vectors according to predetermined values.
Vectors are extended to be of length "iter".
Income is predetermined for t = [0, 1, 2, 3].
Consumption is predetermined for t=[0, 1].
Consumption is calculated based on income for t=[2, 3].
Inventory is calculated to be of ideal value for t=[0, 1, 2, 3] based on Consumption.
Predicted is calculated to be equivalent to Consumption for t=[0, 1, 2, 3].
Inventory_produced is calculated to be difference in Inventory.
Investment is calculated to be the difference between Income, Consumption, and Predicted.
'''
def mapping(y0, y1, y2, y3, c0, c1, s, k, v, q, iter):
    #Initialization
    Income = np.append([y0, y1, y2, y3], np.ones(iter-4))
    Consumption = np.append([c0, c1, consume(y1, y0, s), consume(y2, y1, s)], np.ones(iter-4))
    Inventory = Consumption * k
    Predicted = Consumption 
    Inventory_produced = np.ones(iter)
    for i in range(1, 4):
        Inventory_produced[i] = Inventory[i] - Inventory[i-1]
    Investment = np.ones(iter)
    for i in range(4):
        Investment[i] = Income[i] - Consumption[i] - Predicted[i]
    Adaptive = np.ones(iter)
    Adaptive[3] = adapt(Consumption[i-1], Consumption[i-2], Consumption[i-3])
    #Simulation
    for i in range(4, iter):
        Consumption[i] = consume(Income[i-1], Income[i-2], s)
        Investment[i] = invest(Income[i-1], Income[i-2], v, q)
        Predicted[i] = predict(Consumption[i-1], Consumption[i-2], Adaptive[i-1])
        Adaptive[i] = adapt(Consumption[i-1], Consumption[i-2], Consumption[i-3])
        Inventory_produced[i] = invent_purchase(Predicted[i], Inventory[i-1], k)
        Inventory[i] = inventory(Inventory[i-1], Inventory_produced[i], Predicted[i], Consumption[i])
        Income[i] = Predicted[i] + Investment[i] + Inventory_produced[i]
    variable_plot(Income)
    print(Income)

#Parameter and initial condition set up with quasi-periodic/periodic behavior
mapping(100, 110, 120, 130, 80, 90, 0.3, 0.5, 50, 28.5785, 200)
#Parameter and initial condition set up with periodic behavior
#mapping(100, 110, 120, 130, 80, 90, 0.3, 0.5, 50, 35, 100)