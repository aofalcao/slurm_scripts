# slurm_scripts

SLURM scripts, examples and tutorial for executing code with the Computing Resources @DIFCUL

### 

### Test 1 - Checking if everything is working

1. Login into the login node as instructed with your DI credentials
2. Create the test1.sh file as below - replace USERNAME with your actual username

```
#!/bin/bash
#SBATCH --job-name=simple-job
#SBATCH --output=/mnt/storage/admindi/home/USERNAME/slurm_outputs/output.txt
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --partition=compute

echo "Job running on node: $(hostname)"
```

2. execute the script with `sbatch test1.sh`
3. Check if the slurm_outputs in your home directory was created and the `output.txt` has the hostname of the compute node

### Test 2 - Testing and running Python code

This second test will allow you to check how to create and process data that is in your personal storage

1. Do everything as above but use the `test2.sh` file on this shell folder
2. Create the `test1.py` file (from this repo Python folder)
3. run `sbatch test2.sh` for executing the script on the compute node
4. Check if the `output.txt` file on the slurm_outputs folder has been changed
5. Check if in your home directory you have a `GreatFile.txt` created

### Test 3 - Interfacing with the GPUs

This tutorial used pytorch under miniconda. Other libraries might be used but they were not tested

1. download miniconda by running the following code
`curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. Install it by running `bash ~/Miniconda3-latest-Linux-x86_64.sh`
3. Restart the terminal
4. [optional but recommended] create a new conda environment with
   `create -n torch-env -c pytorch pytorch torchvision`
5. activate the torch environment with 
    `conda activate torch-env`
6. Install pytorch
    `conda install -c pytorch pytorch torchvision`

Now within this environment you may be able to run your code on any compute node available. The slurm script should be very similar as the one above, just the python code is different

1. Login into the login node
2. Use the `test3.sh` file on this shell folder
3. Create the `test1.py` file (from this repo Python folder)
4. make sure the the `torch-env`  conda environment is activated as on point 5. above.
5. check the output and verify if the code worked by printing that CUDA is available and printing a random tensor

