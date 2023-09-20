# MCMCNutshell
This repository accompanies the paper 
[Concepts in Monte Carlo sampling](http://arxiv.org/abs/2309.03136)
by Gabriele Tartero and Werner Krauth. It contains Python implementations
for all algorithms discussed there, numbered and named in the same way. 
In every program, $\beta = 1$ is understood.

## Programs and usage
This repository contains thirteen simulations of one particle subject to a
one-dimensional anharmonic potential, both 
at constant energy (Alg. 00) and at constant temperature
(Algs. from 01 to 12), as discussed in the paper. 

The implementation of Alg. 00 is self-contained:
it samples the position of the particle and compares the experimental
histogram with the theoretical result (see Sec. IIA in the paper).

The implementations of Algs. from 01 to 12 all sample the position of the 
particle and store the results in a text file. To compare the experimental
histograms with the theoretical Boltzmann distribution, it suffices to 
produce the data with the concerned program and then to run the script 
[histograms.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/histograms.py).

All programs can be executed with any Python3 implementation 
(e.g., standard [CPython](https://www.python.org/) or 
[PyPy3](https://www.pypy.org/)). The scripts
[00_isolated-dynamics.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/00_isolated-dynamics.py) 
and [histograms.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/histograms.py)
rely both on [NumPy](https://numpy.org/) and 
[Matplotlib](https://matplotlib.org/) to produce the histograms, while
all other programs do not have any further requirements. 


## Authors
The authors of this project are:
* Gabriele Tartero 
([gabriele.tartero@phys.ens.fr](mailto:gabriele.tartero@phys.ens.fr));
* Werner Krauth ([werner.krauth@ens.fr](mailto:werner.krauth@ens.fr)).

For any question about the MCMCNutshell software package, or the related
paper,
please raise an issue here on GitHub or contact us via e-mail.

## License
This project is licensed under the GNU General Public License, 
version 3 (see the 
[LICENSE](https://github.com/jellyfysh/MCMCNutshell/blob/master/LICENSE) 
file).

