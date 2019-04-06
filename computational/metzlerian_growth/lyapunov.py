import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def growth(dYt1, dYt2, dYt3, dYt5, dYt6, s, k, v, q):
    dYt = (dYt1 / v) / ( (dYt1 / v)**4 + q) - (dYt2 / v) / ( (dYt2 / v)**4 + q) + ((k+1)/3) * ((1-s)*(dYt2-dYt5)+s*(dYt3-dYt6)) + (1-s)*dYt2 + s*dYt3
    return dYt
def partial1(dYt1, s, k, v, q):
    return ((1)/(v * (q+((dYt1**4)/v**4)))) - ((4*dYt1**4)/(v**5*(q+((dYt1**4)/v**4))))
def partial2(dYt2, s, k, v, q):
    return 1 + ((k+1)*(1-s))/3 - s + (4*dYt2**4)/(v**5*(q+((dYt2**4/v^4))) - (1)/(v*(q+((dYt2**4/v^4)))))
def jacobianmake(dYt1, dYt2, s, k, v, q):
    Jacobian = np.array([[partial1(dYt1,s,k,v,q),partial2(dYt2,s,k,v,q),s+((k+1)/3)*s,0,((k+1)*(s-1))/3,-((k+1)*s)/3],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]])
