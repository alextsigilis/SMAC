import random, math, matplotlib.pyplot as plt

alpha = 0.5
nsteps = 1000000
samples_x = []
samples_y = []
x, y = 0.0, 0.0
for step in range(nsteps):
    if step % 2 == 0:
        while True:
            x = gauss_cut()
            p = math.exp(- alpha * x ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    else:
        while True:
            y = gauss_cut()
            p = math.exp(- alpha * y ** 4 )
            if random.uniform(0.0, 1.0) < p:
                break
    samples_x.append(x)
    samples_y.append(y)
    
plt.hexbin(samples_x, samples_y, gridsize=50, bins=1000)
plt.axis([-1.0, 1.0, -1.0, 1.0])
cb = plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('A2_1')
plt.savefig('plot_A2_1.png')
plt.show()