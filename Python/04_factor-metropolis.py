import math
import random
from potentials import u2, u4

x = 0.0
delta = 0.1

x_pos = []
n_samples = 10 ** 7
for i in range(n_samples):
    new_x = x + random.uniform(-delta, delta)
    delta_u2 = u2(new_x) - u2(x)
    delta_u4 = u4(new_x) - u4(x)
    fil2 = math.exp(-delta_u2)
    fil4 = math.exp(-delta_u4)
    if random.random() < min(1.0, fil2) * min(1.0, fil4):
        x = new_x
    x_pos.append(x)

open("Data/FactorMetropolis.data", "w").write(str(x_pos))
