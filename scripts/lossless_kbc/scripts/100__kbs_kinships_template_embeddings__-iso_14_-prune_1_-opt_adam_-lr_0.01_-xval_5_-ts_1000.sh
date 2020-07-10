#!/bin/bash
#SBATCH --partition=cpu
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=20g
cd /home/XXXXX/neuralogic/
ml Java/1.8.0_202 
java -XX:+UseSerialGC -XX:-BackgroundCompilation -XX:NewSize=2000m -Xms2g -Xmx20g -jar /home/XXXXX/neuralogic/NeuraLogic.jar -t /home/XXXXX/neuralogic/templates/kbs/kinships/template_embeddings -path /home/XXXXX/neuralogic/datasets/kbs/kinships -iso 14 -prune 1 -opt adam -lr 0.01 -xval 5 -ts 1000 -ts 10 -limit 10  -out /home/XXXXX/neuralogic/experiments/lossless_kbc/results/kbs/kinships/template_embeddings/_-iso_14_-prune_1_-opt_adam_-lr_0.01_-xval_5_-ts_1000_dummy