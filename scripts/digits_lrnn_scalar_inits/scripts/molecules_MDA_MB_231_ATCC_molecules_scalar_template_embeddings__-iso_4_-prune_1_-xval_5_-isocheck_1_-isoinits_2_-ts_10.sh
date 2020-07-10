#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=20:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=40g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx40g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/molecules/scalar_template_embeddings -path /home/XXXXX/neuralogic/datasets/molecules/MDA_MB_231_ATCC -iso 4 -prune 1 -xval 5 -isocheck 1 -isoinits 2 -ts 10 -out /home/XXXXX/neuralogic/experiments/digits_lrnn_scalar_inits/results/molecules/MDA_MB_231_ATCC/molecules_scalar_template_embeddings/_-iso_4_-prune_1_-xval_5_-isocheck_1_-isoinits_2_-ts_10