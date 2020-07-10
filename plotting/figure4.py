import json
import os
import numpy as np
import pandas as pd

from grid.loading_results import Loader, Plotter
import matplotlib.pyplot as plt

# %%
cwd = os.getcwd()
results_path = cwd + '/../results'

# %%   CHANGE TO ONE OF THE FOLLOWING 3 FOR THE SUBPLOTS

#A)
experiments_id = "digits_lrnn"
f = open(results_path + "/lossless_lrnn/results/molecules/MDA_MB_231_ATCC/molecules_LRNN_template_embeddings/_-iso_-1_-prune_-1_-opt_adam_-lr_0.01_-xval_5_-ts_1000/export/NeuralTrainingPipe.json")

#B)
# experiments_id = "digits_gnn"
# f = open(results_path + "/lossless_gnn/results/molecules/MDA_MB_231_ATCC/molecules_GNN_template_embeddings/_-iso_-1_-prune_-1_-opt_adam_-lr_0.01_-xval_5_-ts_1000/export/NeuralTrainingPipe.json")

#C)
# experiments_id = "digits_kinships"
# f = open(results_path + "/lossless_kbc/results/kbs/kinships/template_embeddings/_-iso_-1_-prune_-1_-opt_adam_-lr_0.01_-xval_5_-ts_1000/export/NeuralTrainingPipe.json")


total_time = json.load(f)[0]["timing"]["timeTaken"]["seconds"]

# %%

loader = Loader(experiments_id, results_path, split_std=True)
data = loader.load_dataframe()

# %% adhoc REPAIR

data = pd.DataFrame(data.dropna(how="all"))
data = data.sort_values(["iso"])
data = data.reset_index()

pltr = Plotter(data)
# %%

lim = 4

data = data[data['iso'] <= lim]
data = data.set_index("iso")

for suff in ["_mean", "_std"]:
    data["pruning_prunedNeurons" + suff] = data["pruning_prunedNeurons" + suff] / data["pruning_allNeurons" + "_mean"]
    data["compression_compressedNeuronCount" + suff] = data["compression_compressedNeuronCount" + suff] / data[
        "pruning_allNeurons" + "_mean"]
    #

for suff in ["_std", "_mean"]:
    data["pruning_allNeurons" + suff] = data["pruning_allNeurons" + suff] / data["pruning_allNeurons" + "_mean"]

for suff in ["_mean", "_std"]:
    data["pruning_totalTimeTaken" + suff] = data["pruning_totalTimeTaken" + suff] / total_time
    data["compression_totalTimeTaken" + suff] = data["compression_totalTimeTaken" + suff] / total_time
    #

for suff in ["_std", "_mean"]:
    data["train_time" + suff] = data["train_time" + suff] / total_time

# %%
# cols = ["train_acc", "test_acc", "pruning_allNeurons", "pruning_prunedNeurons", "compression_compressedNeuronCount",
#         "compression_totalTimeTaken", "pruning_totalTimeTaken", "train_time"]
cols = ["train_acc", "test_acc", "pruning_prunedNeurons", "compression_compressedNeuronCount", "train_time"]
cols_mean = [col + "_mean" for col in cols]
cols_std = [col + "_std" for col in cols]

data[cols_mean].plot.bar(yerr=data[cols_std].values.T, error_kw=dict(ecolor='k'))
# plt.legend(["train_acc","test_acc","#neurons","#pruned","#compressed","train_time"], loc="upper right")

# lgd = plt.legend(["train_acc", "test_acc", "#pruned", "#lifted", "train_time"], loc="center left",
#                  bbox_to_anchor=(1, 0.5), borderaxespad=1)
lgd = plt.legend([])
# plt.show()
# plt.tight_layout(rect=[1,1,0.95,1.2])
# plt.gcf().subplots_adjust(right=0.5)


# %%   CHANGE TO ONE OF THE FOLLOWING 3 FOR THE SUBPLOTS

plt.xlabel("digits\n(LRNN - molecules (MDA dataset))")
# plt.xlabel("digits\n(GCNN - molecules (MDA dataset))")
# plt.xlabel("digits\n(KBE - KBC (Kinships))")

plt.gcf().set_size_inches(4, 6)
plt.tight_layout()
plt.savefig(results_path + "/images/" + "iso_vector_" + experiments_id + ".pdf", bbox_extra_artists=(lgd))
plt.show()