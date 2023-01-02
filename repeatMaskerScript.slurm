#!/bin/sh
#SBATCH --time=15:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --mem-per-cpu=64gb
#SBATCH --partition=Orion


module load anaconda3/2020.11

cd /nobackup/cooper_research/Sangeetha/repeatMasker

/apps/pkg/repeatmasker/4.1.2/RepeatMasker -lib wyeomyia-families.fa wyeomyia.polished.fasta
