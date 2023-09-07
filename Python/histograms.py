import numpy as np
from matplotlib import pyplot
import glob
import math
from potentials import u

pyplot.rcParams["text.usetex"] = True
pyplot.xlabel(r"$x$", fontsize=20)
pyplot.ylabel(r"$\pi_{24}(x)$", fontsize=20)

for file in glob.glob("Data/*.data"):
    label = file.split("Data")[1][1:-5]
    data = np.array(eval(open(file).readline()))
    bins_x = np.linspace(min(data), max(data), 100)
    pyplot.hist(data, bins_x, label=label, density=True, histtype="step")

norm = 1.0 / 1.93525
boltzmann_dist = np.array([norm * math.exp(-u(x)) for x in bins_x])
pyplot.plot(bins_x, boltzmann_dist, label="Boltzmann")

pyplot.legend(fontsize=18)
pyplot.show()
