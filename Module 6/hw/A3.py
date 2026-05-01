import random, math, matplotlib.pyplot as plt

alpha = 0.5
nsteps = 1000000
samples_x = []
samples_y = []
x, y = 0.0, 0.0
for step in range(nsteps):
    xnew = gauss_cut()#random.uniform(-1.0, 1.0)
    ynew = gauss_cut()#random.uniform(-1.0, 1.0)
    #exp_new = - 0.5 * (xnew ** 2 + ynew ** 2) - alpha * (xnew ** 4 + ynew ** 4)
    #exp_old = - 0.5 * (x ** 2 + y ** 2) - alpha * (x ** 4 + y ** 4)
    p = min(1, (pi(xnew, ynew) / g(xnew, ynew)) * (g(x,y) / pi(x, y)))
    if random.uniform(0.0, 1.0) < p:
        x = xnew
        y = ynew
    samples_x.append(x)
    samples_y.append(y)

plt.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
plt.axis([-1.0, 1.0, -1.0, 1.0])
cb = plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('A3_1')
plt.savefig('plot_A3_1.png')
plt.show()