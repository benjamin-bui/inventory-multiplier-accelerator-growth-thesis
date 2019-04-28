import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
from sympy.solvers import solve
from sympy import Symbol
from sympy.plotting import plot3d

#Plots investment curve given p and q
def investment(v, q, lower, upper, points):
    xaxis = np.linspace(lower, upper, points)
    yaxis = np.ones(points)
    for i in range(points):
        yaxis[i] = (xaxis[i] / v) / ((xaxis[i] / v)**4 + q)
    fig = plt.figure(dpi=1200)
    #Time series of mapping
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xaxis, yaxis, c='blue', linewidth=0.5)
    ax1.set_xlabel('$Y_{t-1}-Y_{t-2}$')
    ax1.set_ylabel('$I_t$')

#Solves for maximal investment given p and q
def maximum(v, q):
    return ((3 ** (3 / 4)) / (4 * q ** (3 / 4) ))

#Solves for the full width at half maximum given v, q, and maximal investment using sympy symbolic algebra. Results of solve for this function are functionally identical to results in Mathematica
def width(v, q):
    max = maximum(v, q)
    half = max / 2
    Y = Symbol('Y')
    solutions = solve( (Y / v) / ((Y / v) ** 4 + q) - half, Y)
    halfwidth = abs(solutions[1]-solutions[0])
    return halfwidth

#Plots maximal investment given a range of v and q
def max_investment(lowerv, upperv, lowerq, upperq, points):
    fig = plt.figure(dpi=1200)
    ax1 = fig.add_subplot(1, 1, 1)
    v = np.linspace(lowerv, upperv, points)
    q = np.linspace(lowerq, upperq, points)
    maximuminv = np.ones(points)
    for i in range(points):
        maximuminv[i] = maximum(v[i], q[i])
    ax1.plot(q, maximuminv, c='blue', linewidth=0.5)
    ax1.minorticks_on()
    ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    ax1.set_xlabel('$q$')
    ax1.set_ylabel('Maximal Investment')

#Plots the Full Width at Half Max with a 3-dimensional tirangular surface plot
def width_investment(lowerv, upperv, lowerq, upperq, points):
    fig = plt.figure(dpi=1200)
    ax = plt.axes(projection='3d')
    v = np.linspace(lowerv, upperv, points)
    q = np.linspace(lowerq, upperq, points)
    v = np.repeat(v, points)
    q = np.tile(q, points)
    Width = np.ones(points*points)
    for i in tqdm(range(points*points)):
        Width[i] = width(v[i], q[i])
    ax.plot_trisurf(v, q, Width, linewidth=0.2, antialiased=True)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax.set_xlabel('$v$')
    ax.set_ylabel('$q$')
    ax.set_zlabel('FWHM')
investment(500, 0.001, -300, 300, 10000)
plt.savefig('./manuscript/figures/metzlerian_growth/investment.eps', dpi=1200)
max_investment(0, 2000, 0.0001, 0.002, 10000)
plt.savefig('./manuscript/figures/metzlerian_growth/maxinvestment.eps', dpi=1200)
width_investment(1, 1000, 0.001, 0.002, 50)
plt.savefig('./manuscript/figures/metzlerian_growth/widthinvestment.eps', dpi=1200)

