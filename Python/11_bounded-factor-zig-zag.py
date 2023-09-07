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
    q_2 = n + 1.0
    q_4 = (n + 1.0) ** 3
    sigma_tilde = sigma
    delta_u2_tilde = -math.log(random.random())
    delta_u4_tilde = -math.log(random.random())
    x_ev2 = x_0 + sigma * (delta_u2_tilde / q_2)
    x_ev4 = x_0 + sigma * (delta_u4_tilde / q_4)
    if min(abs(x_ev2), abs(x_ev4)) > n + 1.0:
        x_ev = sigma * (n + 1.0)
    elif abs(x_ev2) < abs(x_ev4):
        x_ev = x_ev2
        if random.random() < abs(x_ev) / q_2:
            sigma_tilde = -sigma
    else:
        x_ev = x_ev4
        if random.random() < abs(x_ev) ** 3 / q_4:
            sigma_tilde = -sigma
    t_ev = t + abs(x_ev - x)
    for time in range(math.ceil(t), math.floor(t_ev) + 1):
        x_pos.append(x + sigma * (time - t))
    x = x_ev
    sigma = sigma_tilde
    t = t_ev

open("Data/BoundedFactorZig-zag.data", "w").write(str(x_pos))
