#!/bin/bash
#SBATCH --job-name=simple-job
#SBATCH --output=/mnt/storage/admindi/home/rgoncalves/slurm_outputs/output.txt
#SBATCH --ntasks=1
#SBATCH --partition=compute
#SBATCH --gres=gpu:2

# Run the Python script
python sample-allgpus.py
