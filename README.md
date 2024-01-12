## MCMCNutshell
This repository accompanies the article 
[Concepts in Monte Carlo sampling](https://github.com/jellyfysh/MCMCNutshell/blob/master/Concepts_in_Monte_Carlo_sampling.pdf)
by Gabriele Tartero and Werner Krauth. It contains all the supplementary 
material discussed in Appendix B.  

This article may be downloaded for personal use only. 
Any other use requires prior permission of the authors and AIP Publishing. 
This article appeared in American Journal of Physics, Volume 92, Issue 1
(January 2024) and may be found also [here](https://doi.org/10.1119/5.0176853).

### Mathematica notebook
The [Mathematica directory](https://github.com/jellyfysh/MCMCNutshell/blob/master/Mathematica) 
contains a Mathematica notebook, 
both in .nb and .pdf formats, that can be used to reproduce the 
mathematical results presented in Appendix A.

### Python programs
The [Python directory](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python) 
contains thirteen simulations of one particle 
subject to a one-dimensional anharmonic potential, both 
at constant energy (Algorithm 0) and at constant temperature
(Algorithms from 1 to 12), as discussed in the paper. 
In every program, $\beta = 1$ is understood.

The implementation of Algorithm 0 is self-contained:
it samples the position of the particle and compares the experimental
histogram with the theoretical result, given by Equation (7) in Section IIA.

Algorithms from 1 to 12 all sample the position of the 
particle and store the results in a text file. To compare the experimental
histograms with the theoretical Boltzmann distribution, it suffices to 
produce the data with the concerned program and then run the script 
[histograms.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/histograms.py).

All programs can be executed with any Python3 implementation 
(e.g., standard [CPython](https://www.python.org/) or 
[PyPy3](https://www.pypy.org/)). The scripts
[00_isolated-dynamics.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/00_isolated-dynamics.py) 
and [histograms.py](https://github.com/jellyfysh/MCMCNutshell/blob/master/Python/histograms.py)
rely both on [NumPy](https://numpy.org/) and 
[Matplotlib](https://matplotlib.org/) to produce the histograms, while
all other programs do not have any further requirements. 


### Authors
The authors of this project are:
* Gabriele Tartero 
([gabriele.tartero@phys.ens.fr](mailto:gabriele.tartero@phys.ens.fr));
* Werner Krauth ([werner.krauth@ens.fr](mailto:werner.krauth@ens.fr)).

For any question about the MCMCNutshell software package, or the related
paper,
please raise an issue here on GitHub or contact us via e-mail.

### License
This project is licensed under the GNU General Public License, 
version 3 (see the 
[LICENSE](https://github.com/jellyfysh/MCMCNutshell/blob/master/LICENSE) 
file).

