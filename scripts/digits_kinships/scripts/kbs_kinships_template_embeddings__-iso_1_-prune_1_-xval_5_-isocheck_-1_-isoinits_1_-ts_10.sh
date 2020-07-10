#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=10:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=20g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx20g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/kbs/kinships/template_embeddings -path /home/XXXXX/neuralogic/datasets/kbs/kinships -iso 1 -prune 1 -xval 5 -isocheck -1 -isoinits 1 -ts 10 -out /home/XXXXX/neuralogic/experiments/digits_kinships/results/kbs/kinships/template_embeddings/_-iso_1_-prune_1_-xval_5_-isocheck_-1_-isoinits_1_-ts_10