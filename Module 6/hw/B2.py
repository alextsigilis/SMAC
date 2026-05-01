import random, math, matplotlib.pyplot as plt

def levy_harmonic_path(xstart: float, 
                       xend: float,
                       dtau:float,
                       N: int
                      ) -> list[float]:
    """
    Generate a Levy bridge (harmonic-oscillator conditioned path) from xstart to xend.
    
    Parameters
    -----------
    xstart : float
        position at the left endpoint (x[0]).
    xend : float
        fixed position at the right endpoint (x[N-1]).
    dtau : float
        imaginary-time step between adjacent beads (must be > 0).
    N : int
        total number of beads in the path (N >= 2).

    Returns:
    ---------
    list[float]
        list of N floats giving the sampled path positions in order.

    """
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

def rho_free(x, y, beta):
    return math.exp(-(x - y) ** 2 / (2.0 * beta))

beta = 20.0
N = 80
Ncut = N // 2
dtau = beta / N
delta = 1.0
n_steps = 1_000_000
x = [5.0] * N
data = []
for step in range(n_steps):
    x = levy_harmonic_path(x[0], x[0], dtau, N)
    x = x[Ncut:] + x[:Ncut]
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])

# Plot histogram
plt.hist(data, density=True, bins=100, label='QMC', color='white', edgecolor='black')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
plt.plot(list_x, list_y, '--', color='black', label='analytic')
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$\\pi(x)$ (normalized)')
plt.title('levy_harmonic_path (beta=%s, N=%i)' % (beta, N))
plt.xlim(-2, 2)
plt.savefig('hw/plot_B2_beta%s.png' % beta)
plt.show()