import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.linalg import sqrtm

def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt
def mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    #Initialize vectors
    dY = np.append([dY0, dY1, dY2, dY3, dY4, dY5], np.zeros(iter-6))
    #Simulate
    for t in range(6, iter):
        dY[t] = growth(dY[t-1], dY[t-2], dY[t-3], dY[t-5], dY[t-6], s, k, v, q,)
    return dY
def partial1(dYt1, s, k, v, q):
    return ((1)/(v * (q+((dYt1**4)/v**4)))) - ((4*dYt1**4)/(v**5*(q+((dYt1**4)/v**4))))
def partial2(dYt2, s, k, v, q):
    return 1 + ((k+1)*(1-s))/3 - s + (4*dYt2**4)/(v**5*(q+((dYt2**4/v**4))) - (1)/(v*(q+((dYt2**4/v**4)))))
def jacobianmake(dYt1, dYt2, s, k, v, q):
    return np.array([[partial1(dYt1,s,k,v,q),partial2(dYt2,s,k,v,q),s+((k+1)/3)*s,0,((k+1)*(s-1))/3,-((k+1)*s)/3],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]])
def lyapunov(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter):
    dY = mapping(dY0, dY1, dY2, dY3, dY4, dY5, s, k, v, q, iter)
    DG = jacobianmake(dY[1], dY[0], s, k, v, q)
    for i in range(2, iter):
        DG = np.matmul(DG, jacobianmake(dY[i], dY[i-1], s, k, v, q))
    lymatrix = np.matmul(np.matrix.transpose(DG), DG)
    for i in range(2, iter):
        lymatrix = sqrtm(lymatrix)
    eigen = np.linalg.eigvals(lymatrix)
    lyexp = np.log(eigen)
    maxlyexp = np.amax(lyexp)
    print(lymatrix)
    return maxlyexp
def slyplot(lower, upper, points, dY0, dY1, dY2, dY3, dY4, dY5, k, v, q, iter):
    #Plot set up
    fig = plt.figure(dpi=1200)
    ax = fig.add_subplot(111)
    #Generate distribution of parameter
    s = np.linspace(lower, upper, points)
    xaxis = s
    yaxis = np.ones(points)
    for j in tqdm(range(points)):
        yaxis[j] = lyapunov(dY0, dY1, dY2, dY3, dY4, dY5, s[j], k, v, q, iter)
    ax.plot(xaxis, yaxis, ',k', alpha=0.25)
    #Labelling
    ax.minorticks_on()
    ax.set_xlabel('$s$')
    ax.set_ylabel('$\dot Y$')


slyplot(0.5, 1, 1000, 10, 120, 110, 100, 105, 107, 0.3, 500, 0.001, 300)
plt.savefig('./manuscript/figures/metzlerian_growth/slyapunov.eps', dpi=1200)
