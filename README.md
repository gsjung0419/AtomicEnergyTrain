# AtomicEnergyTrain
The repository includes lammps inputs with the trained model (best0.pt), which is the final model.
The methods are explained in the following paper:

## Atomic Energy Accuracy of Neural Network Potentials: Harnessing Pre-training and Transfer Learning

**1. Ten_final**
   Example and log file for the tensile loading of 32 atoms nickel with NNP (final model after transfer learning)
   To run this code, you need to install following codes
   
    -. Install https://github.com/gsjung0419/LMPTorch
   
    -. Install https://github.com/aiqm/torchani
   
    -. MPI (MPICH or OPENMPI), with mpi4py

**2. Training Tutorial** with atomic energy from empirical potentials will be available chapter 3, once the paper is accepted: https://github.com/gsjung0419/TorchANITutorials  

**3.  Selected ~2,500 configurations** through active learning ("Data Distillation for Neural Network Potentials toward Foundational Dataset", https://arxiv.org/abs/2311.05407), is available in the tutorial. 

**4. DFT data** will be available with other ongoing sampling (Gas phase and shear loading). 
