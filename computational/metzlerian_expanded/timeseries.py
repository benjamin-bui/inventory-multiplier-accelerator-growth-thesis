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
    Y = I + S + U + G
    return Y

'''
Solves for government expenditure. Expenditure increases during recessions and increases during booms.
Current equation for expenditure is naively created, will be updated with more research
Concave and decreasing function
'''
def government(g, Y):
    G = g / Y
    return G

#Solves for consumption in terms of income and taxes
def consumption(b, Y, T):
    C = b * (Y - T)
    return C

#Solves for heterogenous expectation weighting based on steady state income
def weight(Cbar, Clag)
    w = 1 / (1 + d * (Cbar - Clag) )
    return w

#Solves expected consumption as a weighted average
def averageexpec(Ue, Ur, w):
    U = w * Ue + (1 - w) * Ur
    return U

#Solves regressive expectation outcome
def rexpec(Cbar, Clag, f):
    Ur = Clag + f * (Cbar - Clag)
    return Ur

#Solves extrapolative expectation outcome
def eexpec(Cbar, Clag, c):
    Clag + c * (Clag - Cbar)
    return Ue

#Solves desired level of inventory
def desinventory(k, U)
    Qhat = k * U
    return Qhat

#Solves actual level of inventory
def actinventory(Qhat, C, U)
    Q = Qhat - (C - U)




