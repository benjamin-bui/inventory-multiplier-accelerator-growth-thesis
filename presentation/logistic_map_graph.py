from pylab import show, scatter, xlim, ylim
from random import randint

iter = 1000         # Number of iterations per point
seed = 0.5          # Seed value for x in (0, 1)
spacing = .0001     # Spacing between points on domain (r-axis)
res = 8             # Largest n-cycle visible

# Initialize r and x lists
rlist = []
xlist = []

def logisticmap(x, r):

    return x * r * (1 - x)

# Return nth iteration of logisticmap(x. r)
def iterate(n, x, r):

    for i in range(1,n):
        x = logisticmap(x, r)

    return x

# Generate list values -- iterate for each value of r
for r in [i * spacing for i in range(int(1/spacing),int(4/spacing))]:
   rlist.append(r)
   xlist.append(iterate(randint(iter-res/2,iter+res/2), seed, r))

scatter(rlist, xlist, s = .01)
xlim(0.9, 4.1)
ylim(-0.1,1.1)
show()
