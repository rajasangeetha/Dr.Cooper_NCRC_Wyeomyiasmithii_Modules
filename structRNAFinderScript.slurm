#!/bin/sh
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128gb
#SBATCH --partition=Orion


module load structRNAfinder

cd /nobackup/cooper_research/Sangeetha/structRNAFinder

/apps/pkg/structRNAfinder/17.03.29/bin/structRNAfinder -i wyeomyia.polished.fasta -r wyeomyia.report.out -d /projects/cooper_research/Programs/structRNAfinder/Rfam.cm -c 16