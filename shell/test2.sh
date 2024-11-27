#!/bin/bash
#SBATCH --job-name=python101
#SBATCH --output=/mnt/storage/admindi/home/USERNAME/slurm_outputs/output.txt
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --partition=compute

python test1.py
