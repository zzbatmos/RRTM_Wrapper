#!/bin/bash
#SBATCH --job-name=TI_case
#SBATCH --output=slurm.out
#SBATCH --error=slurm.err
#SBATCH --partition=batch
#SBATCH --qos=long+
#SBATCH --time=120:00:00
#SBATCH --constraint=hpcf2013
#SBATCH --mem=max
##SBATCH --array=0-3

##iss=$SLURM_ARRAY_TASK_ID
##python run_rrtm_sw.py $iss >> out${iss}.txt 
python run_rrtm_swlw.py 
