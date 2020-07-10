#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=20g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx20g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/molecules/GNN_template_embeddings -path /home/XXXXX/neuralogic/datasets/molecules/MDA_MB_231_ATCC -iso 4 -prune 1 -xval 5 -isocheck -1 -isoinits 1 -ts 10 -ts 10 -limit 10  -out /home/XXXXX/neuralogic/experiments/digits_gnn/results/molecules/MDA_MB_231_ATCC/molecules_GNN_template_embeddings/_-iso_4_-prune_1_-xval_5_-isocheck_-1_-isoinits_1_-ts_10_dummy