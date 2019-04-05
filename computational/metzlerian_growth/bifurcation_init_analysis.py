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
    results.write(f"Long-run values at bifurcation: {set(np.round(ydat, precis))}; Value Count = {len(set(np.round(ydat, precis)))}.\n")
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

def y0bifurcation(lower, upper, points, dY1, dY2, dY3, dY4, dY5, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $\dot Y_0$ bifurcation: lower={lower}, upper={upper}, points={points}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY0 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY0 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0[j], dY1, dY2, dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def y1bifurcation(lower, upper, points, dY0, dY2, dY3, dY4, dY5, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $\dot Y_1$ bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY1 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY1 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1[j], dY2, dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def y2bifurcation(lower, upper, points, dY0, dY1, dY3, dY4, dY5, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $\dot Y_2$ bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY2 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY2 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2[j], dY3, dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def y3bifurcation(lower, upper, points, dY0, dY1, dY2, dY4, dY5, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $\dot Y_3$ bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY3 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY3 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3[j], dY4, dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def y4bifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY5, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $Y_4$ bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY5={dY5}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY4 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY4 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4[j], dY5, s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

def y5bifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, s, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of $Y_5$ bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, s={s}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    dY5 = np.linspace(lower, upper, points)
    Yaxis = []
    #Solve for each parameter value
    print("dY5 Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5[j], s, k, v, q, iterations)
        lastvalues = Income[-last:]
        Yaxis.extend(lastvalues)
    return(Yaxis)

results = open('./computational/metzlerian_growth/bifur-init_results.txt', 'a+')
Yaxis = y0bifurcation(-400, 400, 10000, 120, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, 0, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, 0, 2, 0)
Yaxis = y1bifurcation(-400, 400, 10000, 100, 110, 100, 105, 107, 0.6, 0.3, 500, 0.001)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, 100, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, 100, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 400, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 260, 1, 0)
lbifurana(-400, 400, 10000, Yaxis, 260, 1, 0)
Yaxis = y2bifurcation(-400, 400, 10000, 100, 120, 100, 105, 107, 0.6, 0.3, 500, 0.001)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, 100, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, 100, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 400, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 260, 1, 0)
lbifurana(-400, 400, 10000, Yaxis, 260, 1, 0)
Yaxis = y3bifurcation(-400, 400, 10000, 100, 120, 110, 105, 107, 0.6, 0.3, 500, 0.001,)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, 200, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, 200, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 400, 1, 0)
Yaxis = y4bifurcation(-400, 400, 10000, 100, 120, 110, 100, 107, 0.6, 0.3, 500, 0.001)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, -140, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, -140, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, -20, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, -20, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 50, 1, 0)
lbifurana(-400, 400, 10000, Yaxis, 50, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, 130, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, 130, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 400, 1, 0)
Yaxis = y5bifurcation(-400, 400, 10000, 100, 120, 110, 100, 105, 0.6, 0.3, 500, 0.001)
lbifurana(-400, 400, 10000, Yaxis, -400, 1, 0)
rbifurana(-400, 400, 10000, Yaxis, -0, 2, 0)
lbifurana(-400, 400, 10000, Yaxis, -0, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 120, 2, 0)
rbifurana(-400, 400, 10000, Yaxis, 300, 1, 0)

results.close()
