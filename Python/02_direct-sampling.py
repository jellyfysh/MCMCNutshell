import random
import math
from potentials import u, u2

x_pos = []
n_samples = 10 ** 7
for i in range(n_samples):
    x = random.gauss(0.0, 1.0)
    y = random.uniform(0.0, math.exp(-u2(x)))
    if y < math.exp(-u(x)):
        x_pos.append(x)

open("Data/Direct.data", "w").write(str(x_pos))
