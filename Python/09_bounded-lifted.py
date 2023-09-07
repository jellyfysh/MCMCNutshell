import math
import random
from potentials import u, u_bound

x = 0.0
delta = 0.1
sigma = random.choice([-1, 1])

x_pos = []
n_samples = 10 ** 7
for i in range(n_samples):
    new_x = x + sigma * random.uniform(0.0, delta)
    delta_u = u(new_x) - u(x)
    delta_u_tilde = u_bound(new_x) - u_bound(x)
    fil = math.exp(-delta_u)
    fil_tilde = math.exp(-delta_u_tilde)
    if random.random() < min(1.0, fil_tilde):
        x = new_x
    else:
        if random.random() > (1.0 - fil) / (1.0 - fil_tilde):
            x = new_x
        else:
            sigma *= -1
    x_pos.append(x)

open("Data/BoundedLifted.data", "w").write(str(x_pos))
