import os, math, random, matplotlib.pyplot as plt, tqdm
from typing import Optional
from tqdm import tqdm

Path = list[float]

def V_anharm(x: float, cubic: float, quartic: float) -> float:
    '''Compute only the anharmonic part of the anharmonic potental at position x.'''
    pot = cubic * x ** 3 + quartic * x ** 4
    return pot

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

cubic, quartic = -0.0, 0.0
beta = 20.0
N = 100
Ncut = N // 2
dtau = beta / N
delta = 1.0
n_steps = 1_000_000
x = [-1.0 for _ in range(N)]
partial_path = [0.0 for _ in range(Ncut)]
x_new = [0.0 for _ in range(N)]
tol = 1e-9

weight = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x))
weight_new = 0.0
data = []

for step in tqdm(range(n_steps), desc='sampling'):
    x_new = levy_harmonic_path(x[0], x[Ncut], dtau, N=Ncut) + x[Ncut:]
    weight_new = math.exp(sum(-V_anharm(a, cubic, quartic) * dtau for a in x_new))
    p_acc = min(1, weight_new / (weight + tol))
    if random.random() <= p_acc:
        for k in range(N): x[k] = x_new[k]
        weight = weight_new
    x = x[1:] + x[:1]
    if step % 100 == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])

# Plot histogram
plt.hist(data, density=True, bins=100, label='Metropolis sampling', color='forestgreen', edgecolor='white')
list_x = [0.1 * a for a in range (-30, 31)]
list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
plt.plot(list_x, list_y, '--', color='maroon', label='analytic')
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$\\pi(x)$ (normalized)')
plt.title('levy_free_path for the anharmonic potential (beta=%s, N=%i)' % (beta, N))
plt.xlim(-2, 2)
os.makedirs('hw', exist_ok=True); plt.savefig('hw/plot_C1_beta%s.png' % beta)
plt.show()