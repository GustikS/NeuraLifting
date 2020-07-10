#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=20:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=20g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx20g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/molecules/LRNN_template_embeddings -path /home/XXXXX/neuralogic/datasets/molecules/MDA_MB_231_ATCC -iso 9 -prune 1 -xval 5 -isocheck 1 -isoinits 2 -ts 10 -out /home/XXXXX/neuralogic/experiments/digits_lrnn_vector/results/molecules/MDA_MB_231_ATCC/molecules_LRNN_template_embeddings/_-iso_9_-prune_1_-xval_5_-isocheck_1_-isoinits_2_-ts_10