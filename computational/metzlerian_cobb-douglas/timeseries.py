import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import statistics
from tqdm import tqdm
import scipy

'''
Expanded metzlerian inventory business cycle model based on Westerhoff model
National income is a sum of:
    Production for consumption/sale is U
    Production for stock is S
    Production for investment goods is I
    Production for government is D
Model assumes that government is not budget neutral but is relatively unconcerned about debt levels
Model assumes that government budget is counter-cyclical (relatively realistic)
'''

#Define income as the sum of production outputs.
def metzlerian(I, S, U, G):
    Y = I + S + U 
    return Y

'''
for government expenditure. Expenditure increases during recessions and increases during booms.
Current equation for expenditure is naively created, will be updated with more research
Concave and decreasing function
'''
def government(g, Y):
    G = g / Y
    return G

#Consumption in terms of income and taxes
def consumption(b, Y, T):
    C = b * (Y - T)
    return C

#Heterogenous expectation weighting based on steady state income
def weight(Cbar, Clag)
    w = 1 / (1 + d * (Cbar - Clag) )
    return w

#Expected consumption as a weighted average
def averageexpec(Cbar, Clag, f, c, d):
    Ur = Clag + f * (Cbar - Clag)
    Ue = Clag + c * (Clag - Cbar)
    w = 1 / (1 + d * (Cbar - Clag) 
    U = w * Ue + (1 - w) * Ur
    return U

#Desired level of inventory
def desinventory(k, U)
    Qhat = k * U
    return Qhat

#Actual level of inventory
def actinventory(Qhat, C, U)
    Q = Qhat - (C - U)

#Predicted income level 
def predinc(Ylag, Ybar, h, j, p)
    Pr = Ylag + j * (Ybar - Ylag)
    Pe = Ylag + h * (Ylag - Ybar)
    v = 1 / (1 + p * (Ybar - Ylag) )
    P = v * Pe + (1 - v) * Pr
    return P

#Current capital
def capital(Ilag, delta, Klag):
    K = Ilag + (1 - delta) * Klag
    return K

#Investment 
def invest(Pfut, L, Klag, alpha, delta):
    I = ((Pfut)(L ** (alpha - 1))) ** alpha - (1 - delta) ** Klag
    return I

#Solves for timeseries plot
def timeseries():
    


