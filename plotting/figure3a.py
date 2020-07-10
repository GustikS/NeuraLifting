import os
import numpy as np
import pandas as pd

from grid.loading_results import Loader, Plotter
import matplotlib.pyplot as plt
import json

# %%
cwd = os.getcwd()
results_path = cwd + '/../results'

experiments_id = "digits_lrnn_scalar"
f = open(results_path + "/lrnn_scalar/results/molecules/MDA_MB_231_ATCC/molecules_scalar_template_embeddings/_-iso_-1_-prune_-1_-opt_adam_-lr_0.01_-xval_5_-ts_1000/export/NeuralTrainingPipe.json")
total_time_scalar = json.load(f)["timing"]["timeTaken"]["seconds"]


loader = Loader(experiments_id, results_path, split_std=True)
data = loader.load_dataframe()

# %% adhoc REPAIR

data = pd.DataFrame(data.dropna(how="all"))
data['iso'] = pd.to_numeric(data["iso"])
data = data.sort_values(["iso"])
data = data.reset_index()

pltr = Plotter(data)

# %%
data = data[data['iso'] <= 10]
data = data.set_index("iso")

for suff in ["_mean", "_std"]:
    data["pruning_prunedNeurons" + suff] = data["pruning_prunedNeurons" + suff] / data["pruning_allNeurons" + "_mean"]
    data["compression_compressedNeuronCount" + suff] = data["compression_compressedNeuronCount" + suff] / data[
        "pruning_allNeurons" + "_mean"]
    #

for suff in ["_std", "_mean"]:
    data["pruning_allNeurons" + suff] = data["pruning_allNeurons" + suff] / data["pruning_allNeurons" + "_mean"]

for suff in ["_mean", "_std"]:
    data["pruning_totalTimeTaken" + suff] = data["pruning_totalTimeTaken" + suff] / total_time_scalar
    data["compression_totalTimeTaken" + suff] = data["compression_totalTimeTaken" + suff] / total_time_scalar
    #

for suff in ["_std", "_mean"]:
    data["train_time" + suff] = data["train_time" + suff] / total_time_scalar

# %%
cols = ["train_acc", "test_acc", "pruning_prunedNeurons", "compression_compressedNeuronCount", "train_time"]
cols_mean = [col + "_mean" for col in cols]
cols_std = [col + "_std" for col in cols]

# data[cols_mean].plot.bar(yerr=data[cols_std].values.T, error_kw=dict(ecolor='k'))
# plt.legend(["train_acc", "test_acc", "#pruning", "#lifting", "train_time"], loc="upper right", framealpha=0.99)
# plt.legend(["train_acc","test_acc","#pruned","#compressed","train_time"], loc=(1.01,0.67))
# plt.xlabel("digits")
# plt.show()
# pltr.save(results_path + "/images/" + "iso_scalar_all2")

# %% plotting

x = range(1, 11)

for mean, std in zip(cols_mean, cols_std):
    pltr.area_plot(x, data[mean], data[std],plt.gca())


plt.xlabel("digits\n(LRNN - molecules (MDA dataset))")
plt.grid()
plt.legend(["train_acc","test_acc","#pruning","#lifting","train_time"], loc="upper right", framealpha=0.98)
plt.tight_layout()
plt.gcf().set_size_inches(6, 5.2)
plt.savefig(results_path + "/images/" + "iso_scalar_all.pdf")
plt.show()
