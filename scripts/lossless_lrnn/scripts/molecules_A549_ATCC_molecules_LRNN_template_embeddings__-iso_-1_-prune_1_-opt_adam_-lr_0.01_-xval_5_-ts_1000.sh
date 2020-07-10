#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=23:59:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=30g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx30g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/molecules/LRNN_template_embeddings -path /home/XXXXX/neuralogic/datasets/molecules/A549_ATCC -iso -1 -prune 1 -opt adam -lr 0.01 -xval 5 -ts 1000 -out /home/XXXXX/neuralogic/experiments/lossless_lrnn/results/molecules/A549_ATCC/molecules_LRNN_template_embeddings/_-iso_-1_-prune_1_-opt_adam_-lr_0.01_-xval_5_-ts_1000