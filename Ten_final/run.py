import os
from lammps import lammps
import torch
import torchani
import numpy as np

os.system("rm geo*.xyz ss*.dat sd.dat")
lmp=lammps()
lmp.file("ten.in")

