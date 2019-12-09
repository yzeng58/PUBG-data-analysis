#!/bin/bash
#SBATCH --mail-user=zxu444@stat.wisc.edu
#SBATCH --mail-type=ALL
#SBATCH -p short
#SBATCH -t 2-00:00:00
#SBATCH -n 4
#SBATCH --array=1-6
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2600M
#SBATCH --output="slurm/slurm-%A_%a.out"
n=$SLURM_ARRAY_TASK_ID

python weapon_summary.py $n
