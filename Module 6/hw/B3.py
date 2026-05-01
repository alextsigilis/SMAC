import math, random, matplotlib.pyplot as plt
from typing import Optional

Path = list[float]
random.seed(42)

def levy_harmonic_path(
    start: float,
    end: float,
    dtau:float,
    out: Optional[Path] = None,
    N: Optional[int] = None
) -> list[float]:
    """
    Generate a Levy bridge (harmonic-oscillator conditioned path) from xstart to xend.
    
    Parameters
    -----------
    start : float
        Left endpoint value (x[0]).
    end : float
        Right endpoint value (x[N-1]).
    dtau : float
        Imaginary-time step between adjacent beads; must be > 0.
    out : Optional[Path], optional
        Mutable sequence to receive the sampled positions. If provided, its length
        determines N unless N is also given; when provided its length must be >= 2.
        If None, a new list of length N is allocated.
    N : Optional[int], optional
        Number of beads (path length). If provided, a new list of this length is
        allocated when out is None. If both out and N are given, N is used only
        when out is None.

    Returns:
    ---------
    list[float]
        Length-N list of sampled positions representing the Lévy bridge from
        start to end (inclusive).

    """
    # Parse input
    if out is None and N is None:
        raise Exception("out or N must be provided")
    if out is None:
        out = [0.0 for _ in range(N)]
    if N is None:
        N = len(out)
    # Sample path
    out[0] = start
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = ( 1.0 / math.tanh(dtau) ) + ( 1.0 / math.tanh(dtau_prime) )
        Ups2 = ( out[k - 1] / math.sinh(dtau) 
                 + end / math.sinh(dtau_prime) )
        out[k] = random.gauss(Ups2 / Ups1,
                              1.0 / math.sqrt(Ups1))
    return out

beta = 20.0
sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2))
N = 80
Ncut = N // 2
dtau = beta / N
delta = 1.0
n_steps = 1_000_000
x = [0.0 for _ in range(N)]
data = []
for step in range(n_steps):
    x0 = random.gauss(mu=0.0, sigma=sigma)
    levy_harmonic_path(x0, x0, dtau, out=x)
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])

# Plot histogram
plt.hist(data, density=True, bins=100, label='QMC', color='grey', edgecolor='white')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
plt.plot(list_x, list_y, '--', color='maroon', label='analytic')
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$\\pi(x)$ (normalized)')
plt.title('levy_harmonic_path (beta=%s, N=%i)' % (beta, N))
plt.xlim(-2, 2)
plt.savefig('hw/plot_B3_beta%s.png' % beta)
plt.show()