import os
import statistics

import numpy as np
import pandas as pd

from grid.loading_results import Loader, Plotter
import matplotlib.pyplot as plt

cwd = os.getcwd()
results_path = cwd + '/../results'

# %%

experiments_id = "digits_lrnn_vector"

loader = Loader(experiments_id, results_path)
data = loader.load_dataframe(posprocess=False)

# %% adhoc repair

data = pd.DataFrame(data.dropna(how="all"))
data['iso'] = pd.to_numeric(data["iso"])
data = data.sort_values(["iso"])
data = data.reset_index()

data['compression_preventedByIsoCheck'] = data['compression_preventedByIsoCheck'] - 1

# %% plotting

pltr = Plotter(data)

pltr.normal_plot(data['compression_preventedByIsoCheck'], data['iso'], xlabel="digits", ylabel="#value clashes",
                 legend="vectorized", title="", color='m')

# %%

experiments_id = "digits_lrnn_scalar_inits"

loader = Loader(experiments_id, results_path)
data = loader.load_dataframe(posprocess=False)

# %%

folds = data['compression_preventedByIsoCheck'].tolist()
c = [str(statistics.mean(fold)) + " +- " + str(statistics.stdev(fold)) for fold in folds]
data['compression_preventedByIsoCheck'] = pd.Series(c)
# %% adhoc REPAIR

data = pd.DataFrame(data.dropna(how="all"))
data['iso'] = pd.to_numeric(data["iso"])
data = data.sort_values(["iso", "isoinits"])
data = data.reset_index()


# %% plotting


pltr = Plotter(data)

for i in [3, 2, 1]:
    pltr.conf_plot(data[data["isoinits"] == i]['compression_preventedByIsoCheck'], data[data["isoinits"] == i]['iso'],
                   xlabel="digits\n(LRNN - molecules (MDA dataset))", ylabel="#value clashes",
                   legend="inits=" + str(i), title="", color=['r', 'g', 'y'][i - 1])


plt.title("")
plt.yscale("symlog")
# plt.gca().set_ylim([0,1e8])

plt.gcf().set_size_inches(6.7, 5.5)
plt.grid()
pltr.save(results_path + "/images/" + "isocheck_combined")
