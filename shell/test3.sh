#!/bin/bash
#SBATCH --job-name=testing_pytorch
#SBATCH --output=/mnt/storage/admindi/home/USERNAME/slurm_outputs/output_torch.txt
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --partition=compute

python torchtest.py
