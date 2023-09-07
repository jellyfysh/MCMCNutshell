import numpy as np
from matplotlib import pyplot
import math
from potentials import u

amp = 4.0
delta_t = 10 ** (-6)
t_tot = 10.0

x = -amp
v = 0.0
t = 0.0

x_pos = []
while t < t_tot:
    t += delta_t
    new_x = x + v * delta_t
    v = v - (x + x ** 3) * delta_t
    x = new_x
    x_pos.append(x)

pyplot.rcParams["text.usetex"] = True
pyplot.xlabel(r"$x$", fontsize=20)
pyplot.ylabel(r"$\pi^{iso}(x)$", fontsize=20)

bins_x = np.linspace(min(x_pos), max(x_pos), 100)
pyplot.hist(x_pos, bins_x, label="IsolatedDynamics", density=True, histtype="step")

bins_theoretical = np.linspace(0.99 * min(x_pos), 0.99 * max(x_pos), 100)
norm = 1 / 0.887645
landau_dist = np.array([norm * math.sqrt(2 * (u(amp) - u(x))) ** (-1) for x in bins_theoretical])
pyplot.plot(bins_theoretical, landau_dist, label="TheoreticalCurve")

pyplot.legend(fontsize=18)
pyplot.show()
