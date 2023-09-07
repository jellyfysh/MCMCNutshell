import math
import random

x = 0.0
time_ev = 0.0
sigma = 1 if x <= 0.0 else -1

x_pos = []
n_samples = 10 ** 7
while len(x_pos) < n_samples:
    delta_u = -math.log(random.random())
    new_x = sigma * math.sqrt(-1.0 + math.sqrt(1.0 + 4.0 * delta_u))
    new_time_ev = time_ev + abs(new_x - x)
    for t in range(math.ceil(time_ev), math.floor(new_time_ev) + 1):
        x_pos.append(x + sigma * (t - time_ev))
    x = new_x
    time_ev = new_time_ev
    sigma *= -1

open("Data/Zig-zag.data", "w").write(str(x_pos))
