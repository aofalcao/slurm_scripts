#!/bin/bash
#SBATCH --job-name=test-nvidia-smi
#SBATCH --output=/mnt/storage/admindi/home/USERNAME/slurm_outputs/nvidia.smi
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --partition=compute

nvidia-smi

