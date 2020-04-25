#!/usr/bin/env bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --job-name=ps6
#SBATCH --output=slurm-%j-%x.out
#SBATCH --time=0-01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=3

conda deactivate
conda activate bgmp_py3


file1="/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1"
file2="/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2"
file3="/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched"

mkdir -p velveth_dir_31
mkdir -p velveth_dir_41
mkdir -p velveth_dir_49

/usr/bin/time -v velveth velveth_dir_31 31 -shortPaired -fastq $file1 $file2 -short -fastq  $file3
/usr/bin/time -v velveth velveth_dir_41 41 -shortPaired -fastq $file1 $file2 -short -fastq  $file3
/usr/bin/time -v velveth velveth_dir_49 49 -shortPaired -fastq $file1 $file2 -short -fastq  $file3
