import math
import random

x = 0.0
t = 0.0
sigma = random.choice([-1, 1])

x_pos = []
n_samples = 10 ** 7
while len(x_pos) < n_samples:
    x_0 = 0.0 if sigma * x < 0.0 else x
    n = math.floor(abs(x_0))
    q = n + 1.0 + (n + 1.0) ** 3
    sigma_tilde = sigma
    delta_u_tilde = -math.log(random.random())
    x_ev = x_0 + sigma * (delta_u_tilde / q)
    if abs(x_ev) > n + 1.0:
        x_ev = sigma * (n + 1)
    elif random.random() < abs(x_ev + x_ev ** 3) / q:
        sigma_tilde = -sigma
    t_ev = t + abs(x_ev - x)
    for time in range(math.ceil(t), math.floor(t_ev) + 1):
        x_pos.append(x + sigma * (time - t))
    x = x_ev
    sigma = sigma_tilde
    t = t_ev

open("Data/BoundedZig-zag.data", "w").write(str(x_pos))
