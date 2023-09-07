import math
import random

delta_t = 10 ** (-3)
t_tot = 10 ** 4

x = -4.0
v = 0.0
t = 0.0

x_pos = []
while t < t_tot:
    t += delta_t
    new_x = x + v * delta_t
    if x * new_x < 0 and random.random() < 0.5:
        v = -(v / abs(v)) * math.sqrt(-2.0 * math.log(random.random()))
    else:
        v = v - (x + x ** 3) * delta_t
        x = new_x
    x_pos.append(x)

open("Data/ThermostatDynamics.data", "w").write(str(x_pos))
