#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=23:59:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=40g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx40g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/molecules/scalar_template_embeddings -path /home/XXXXX/neuralogic/datasets/molecules/MDA_MB_231_ATCC -iso 5 -prune 1 -xval 5 -isocheck -1 -isoinits 1 -opt adam -lr 0.01 -ts 1000 -out /home/XXXXX/neuralogic/experiments/digits_lrnn_scalar/results/molecules/MDA_MB_231_ATCC/molecules_scalar_template_embeddings/_-iso_5_-prune_1_-xval_5_-isocheck_-1_-isoinits_1_-opt_adam_-lr_0.01_-ts_1000