import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

#Create time series mapping 
def growth(dUt, dIt, dSt):
    dYt = dUt + dIt + dSt
    return dYt
def invest(dYt1, dYt2, v, q):
    dIt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q)
    return dIt
def consume(dYt1, dYt2, s):
    dCt = (1 - s) * dYt1 + s * dYt2
    return dCt
def predict(dCt1, dCt2, dCt3):
    dUt = (dCt1 + dCt2 + dCt3) / 3
    return dUt
def invent(dUt, dCt, k):
    dQt = (k + 1) * dUt - dCt
    return dQt
def pinvent(dUt, dQt1, k):
    dSt = k * dUt - dQt1
    return dSt

#Plot timeseries
def variableplot(Variable):
    fig = plt.figure(dpi=600)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(Variable, c='blue', linewidth=0.5)

def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):

    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    dI = np.zeros(iter)
    dC = np.zeros(iter)
    dU = np.zeros(iter)
    dQ = np.zeros(iter)
    dS = np.zeros(iter)
    for t in range(2, 6):
        dI[t] = invest(dY[t-1], dY[t-2], v, q)
        dC[t] = consume(dY[t-1], dY[t-2], s)
    for t in range(5, 6):
        dU[t] = predict(dC[t-1], dC[t-2], dC[t-3])
        dQ[t] = invent(dU[t], dC[t], k)
    #Simulate
    for t in range(6, iter):
        dI[t] = invest(dY[t-1], dY[t-2], v, q)
        dC[t] = consume(dY[t-1], dY[t-2], s)
        dU[t] = predict(dC[t-1], dC[t-2], dC[t-3])
        dQ[t] = invent(dU[t], dC[t], k)
        dS[t] = pinvent(dU[t], dQ[t-1], k)
        dY[t] = growth(dU[t], dI[t], dS[t])
    return dY

def lbifurana(lower, upper, points, Yaxis, lsearch, period, precis):
    last = 30
    param = np.linspace(lower, upper, points)
    Xaxis = np.repeat(param, last)
    bifurfound = False
    lsearch = np.nonzero(Xaxis >= lsearch)
    lsearch = lsearch[0][0]
    i = lsearch
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
            i += last
    results.write(f"Bifurcation Point Found from {period} cycle\n")
    results.write(f"Bifurcation Point at {Xaxis[i]}\n")
    results.write(f"Long-run values at bifurcation: {set(np.round(ydat, precis))}\n")
    results.write(f"Analysis done rounding to {precis} decimal places\n\n")
    
def rbifurana(lower, upper, points, Yaxis, usearch, period, precis):
    last = 30
    param = np.linspace(lower, upper, points)
    Xaxis = np.repeat(param, last)
    bifurfound = False
    usearch = np.nonzero(Xaxis <= usearch)
    usearch = usearch[0][0]
    i = usearch
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
    results.write(f"Bifurcation Point Found into {period} cycle\n")
    results.write(f"Bifurcation Point at {Xaxis[i]}\n")
    results.write(f"Long-run values at bifurcation: {set(np.round(ydat, precis))}\n")
    results.write(f"Analysis done rounding to {precis} decimal places\n\n")

def sbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, k, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of s bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, k={k}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    s = np.linspace(lower, upper, points)
    Xaxis = np.repeat(s, last)
    Yaxis = []
    #Solve for each parameter value
    print("s Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s[j], k, v, q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                Yaxis = np.append(Yaxis, Income[m])
    return(Yaxis)

def kbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, v, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of k bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, v={v}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    k = np.linspace(lower, upper, points)
    Xaxis = np.repeat(k, last)
    Yaxis = []
    #Solve for each parameter value
    print("k Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k[j], v, q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                Yaxis = np.append(Yaxis, Income[m])
    return(Yaxis)

def vbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, q):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of v bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, q={q} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    v = np.linspace(lower, upper, points)
    Xaxis = np.repeat(v, last)
    Yaxis = []
    #Solve for each parameter value
    print("v Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v[j], q, iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                Yaxis = np.append(Yaxis, Income[m])
    return(Yaxis)

def qbifurcation(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, s, k, v):
    #Print initial conditions of bifurcation to bifur_results.txt
    results.write(f"Initial conditions of q bifurcation: lower={lower}, upper={upper}, points={points}, dY0={dY0}, dY1={dY1}, dY2={dY2}, dY3={dY3}, dY4={dY4}, dY5={dY5}, s={s}, k={k}, v={v} \n\n")
    #Plot set up
    last = 30
    iterations = 3000
    #Generate distribution of parameter
    q = np.linspace(lower, upper, points)
    Xaxis = np.repeat(v, last)
    Yaxis = []
    #Solve for each parameter value
    print("q Bifurcation")
    for j in tqdm(range(points)):
        Income = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q[j], iterations)
        for m in range(iterations):
            if m >= (iterations-last):
                Yaxis = np.append(Yaxis, Income[m])
    return(Yaxis)

results = open('./computational/metzlerian_growth/bifur_results.txt', 'a+')
Yaxis = sbifurcation(0.65, 0.9, 10000, 29, 30 , 50 , 100, 20, 50, 0.3, 500, 0.001)
lbifurana(0.65, 0.9, 10000, Yaxis, 0.65, 2, 0)
Yaxis = kbifurcation(0.1, 0.9, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 500, 0.001)
lbifurana(0.1, 0.9, 10000, Yaxis, 0.1, 2, 0)
Yaxis = vbifurcation(0, 2000, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 0.3, 0.001)
lbifurana(0, 2000, 10000, Yaxis, 550, 2, 0)
rbifurana(0, 2000, 10000, Yaxis, usearch, 1000, 1, 0)
Yaxis = qbifurcation(0, 0.0001, 10000, 29, 30 , 50 , 100, 20, 50, 0.6, 0.3, 500)
lbifurana(0,0.0001, 10000, Yaxis, 0, 0)
results.close()
