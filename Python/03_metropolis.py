import math
import random
from potentials import u

x = 0.0
delta = 0.1

x_pos = []
n_samples = 10 ** 7
for i in range(n_samples):
    new_x = x + random.uniform(-delta, delta)
    delta_u = u(new_x) - u(x)
    fil = math.exp(-delta_u)
    if random.random() < min(1.0, fil):
        x = new_x
    x_pos.append(x)

open("Data/Metropolis.data", "w").write(str(x_pos))
