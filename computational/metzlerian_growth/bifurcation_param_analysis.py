import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Create growth formula
#Time series with mean of last 3 prediction
def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt

#Creates mapping for growth model based on growth function
def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    #Simulate
    for t in range(6, iter):
        dY[t] = growth(dY[t-1], dY[t-2], dY[t-3], dY[t-5], dY[t-6], s, k, v, q,)
    return dY

def lbifurana(lower, upper, points, Yaxis, lsearch, period, precis):
    last = 30
    param = np.linspace(lower, upper, points)
    Xaxis = np.repeat(param, last)
    bifurfound = False
    i = np.nonzero(Xaxis >= lsearch)
    i = i[0][0]
    while bifurfound == False:
        ydat = [Yaxis[i]]
        for j in range(i+1, i+last):
            ydat = np.append(ydat, Yaxis[j])
        count = len(set(np.round(ydat, precis)))
        if count != period:
            print("Bifurcation Point Found Searching")
            bifurfound = True
            print("Period Shift from")
            print(period)
            print("Bifurcation Point at")
            print(Xaxis[i])
            print("Points")
            print(set(np.round(ydat, precis)))
        else:
            i += last
    results.write(f"Bifurcation Point found starting search from {lsearch}, left to right from {period} cycle.\n")
    results.write(f"Bifurcation Point at {Xaxis[i]}.\n")
    results.write(f"Long-run values at bifurcation: {set(np.round(ydat, precis))}; Value Count = {len(set(np.round(ydat, precis)))} \.\n")
    results.write(f"Analysis done rounding to {precis} decimal places.\n\n")
    
def rbifurana(lower, upper, points, Yaxis, usearch, period, precis):
    last = 30
    param = np.linspace(lower, upper, points)
    Xaxis = np.repeat(param, last)
    bifurfound = False
    i = np.nonzero(Xaxis >= usearch)
    i = i[0][0]
    while bifurfound == False:
        ydat = [Yaxis[i]]
        for j in range(i+1, i+last):
            ydat = np.append(ydat, Yaxis[j])
        count = len(set(np.round(ydat, precis)))
        if count != period:
            print("Bifurcation Point Found")
            bifurfound = True
            print("Period Shift from")
            print(period)
            print("Bifurcation Point at")
            print(Xaxis[i])
            print("Points")
            print(set(np.round(ydat, precis)))
        else:
            i -= last
    results.write(f"Bifurcation Point found starting search from {usearch}, right to left into {period} cycle.\n")
    results.write(f"Bifurcation Point Found into {period} cycle.\n")
    results.write(f"Bifurcation Point at {Xaxis[i]}.\n")
    results.write(f"Long-run values at bifurcation: {set(np.round(ydat, precis))}; Value Count = {len(set(np.round(ydat, precis)))}.\n")
    results.write(f"Analysis done rounding to {precis} decimal places.\n\n")

def sbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of s bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    s = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("s Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s[j], k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def kbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of k bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    k = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("k Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k[j], v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def vbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of v bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    v = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("v Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v[j], q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def qbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, v):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of q bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    q = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("q Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q[j], iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

results = open('./computational/metzlerian_growth/bifur_results.txt', 'a+')
Yaxis = sbifurcation(0.1, 0.9, 50000, 100, 120, 110, 100, 105, 107, 0.3, 500, 0.001)
lbifurana(0.65, 0.9, 50000, Yaxis, 0.53, 2, 0)
rbifurana(0.65, 0.9, 50000, Yaxis, 0.53, 2, 0)
Yaxis = kbifurcation(0.1, 0.9, 50000, 100, 120, 110, 100, 105, 107, 0.6, 500, 0.001)
lbifurana(0.1, 0.9, 50000, Yaxis, 0.1, 2, 0)
rbifurana(0.1, 0.9, 50000, Yaxis, 0.9, 2, 0)
Yaxis = vbifurcation(1, 2000, 50000, 100, 120, 110, 100, 105, 107, 0.6, 0.3, 0.001)
lbifurana(1, 2000, 50000, Yaxis, 1, 1, 0)
rbifurana(1, 2000, 50000, Yaxis,  1000, 1, 0)
lbifurana(1, 2000, 50000, Yaxis, 525, 2, 0)
rbifurana(1, 2000, 50000, Yaxis,  525, 2, 0)
Yaxis = qbifurcation(0, 0.0001, 50000, 100, 120, 110, 100, 105, 107, 0.6, 0.3, 500)
rbifurana(0,0.0001, 50000, Yaxis, 0.00008, 1, 0)
results.close()
