import os
import numpy as np
import pandas as pd

from grid.loading_results import Loader, Plotter
import matplotlib.pyplot as plt

# %%

cwd = os.getcwd()
results_path = cwd + '/../results'

#%% CHANGE TO ONE OF THE FOLLOWING 3 FOR THE SUBPLOTS

experiments_id = "lossless_lrnn"
# experiments_id = "lossless_gnn"
# experiments_id = "lossless_kbc"

# %%

headnum = 3 # show only first 3

loader = Loader(experiments_id, results_path, split_std=True)
data = loader.load_dataframe()

# %% adhoc REPAIR

data = pd.DataFrame(data.dropna(how="all"))
data = data.sort_values(["iso"])
# data = data.reset_index()

pltr = Plotter(data)
# %%

iso_on = data[(data['iso'] == 14) & (data['prune'] == 1)]
iso_off = data[(data['iso'] == -1) & (data['prune'] == -1)]

iso_on = iso_on.set_index('dataset').sort_index()
iso_off = iso_off.set_index('dataset').sort_index()

# %%

for suff in ["_std", "_mean"]:
    iso_on["train_time" + suff] = iso_on["train_time" + suff] / iso_off["train_time" + "_mean"]
    iso_off["train_time" + suff] = iso_off["train_time" + suff] / iso_off["train_time" + "_mean"]

# %%
cols = ["train_acc", "test_acc", "train_time"]
cols_mean = [col + "_mean" for col in cols]
cols_std = [col + "_std" for col in cols]

iso_on["compression_mean"] = iso_on["compression_compressedNeuronCount_mean"] / iso_on["pruning_allNeurons_mean"]
iso_on["compression_std"] = iso_on["compression_compressedNeuronCount_std"] / iso_on["pruning_allNeurons_mean"]

iso_on = iso_on[cols_mean + cols_std + ["compression_mean", "compression_std"]]
iso_off = iso_off[cols_mean + cols_std]

merged = pd.merge(iso_on, iso_off, suffixes=('_on', '_off'), left_index=True, right_index=True)
merged = merged.head(headnum)

cols_mean_onoff = []
for m in cols_mean:
    cols_mean_onoff.append(m + "_on")
    cols_mean_onoff.append(m + "_off")

cols_std_onoff = []
for m in cols_std:
    cols_std_onoff.append(m + "_on")
    cols_std_onoff.append(m + "_off")

cols_mean_onoff.remove("train_time_mean_off")
cols_std_onoff.remove("train_time_std_off")

cols_mean_onoff.append("compression_mean")
cols_std_onoff.append("compression_std")

merged[cols_mean_onoff].plot.bar(yerr=merged[cols_std_onoff].values.T, error_kw=dict(ecolor='k'))

# lgd = plt.legend(["train_acc (lifted)","train_acc (base)", "test_acc (lifted)","test_acc (base)","train_time (lifted)", "#neurons (lifted)"], loc="center left", bbox_to_anchor=(1, 0.5), borderaxespad=1)
lgd = plt.legend([])


# choose one of the barplots from Fig. 3

plt.xlabel("molecules\n(LRNN model)")
# plt.xlabel("molecules\n(GCNN model)")
# plt.xlabel("KBC\n(KBEs models)")

# plt.show()

plt.gcf().set_size_inches(4, 7)
plt.tight_layout()
plt.savefig(results_path + "/images/" + "iso_vector_" + experiments_id + ".pdf", bbox_extra_artists=(lgd))
plt.show()