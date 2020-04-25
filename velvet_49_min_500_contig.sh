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



/usr/bin/time -v velvetg velveth_dir_49 -cov_cutoff auto -min_contig_lgth 500
mv /projects/bgmp/gperez8/Bi621/PSs/PS6/velveth_dir_49/contigs.fa /projects/bgmp/gperez8/Bi621/PSs/PS6/velveth_dir_49/contigs_auto_500.fa
