from grid import *

#%%

grid = GridSetup(experiment_id="digits_lrnn",
                 param_ranges={"iso": [1, 2, 3, 4], "prune": [1], "xval": [5],
                               "isocheck": [-1], "isoinits": [1], "ts": [10]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/LRNN_template_embeddings"],
                 walltime="10:00:00",
                 memory_max="20g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="digits_gnn",
                 param_ranges={"iso": [1, 2, 3, 4], "prune": [1], "xval": [5],
                               "isocheck": [-1], "isoinits": [1], "ts": [10]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/GNN_template_embeddings"],
                 walltime="10:00:00",
                 memory_max="20g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="digits_kinships",
                 param_ranges={"iso": [1, 2, 3, 4], "prune": [1], "xval": [5],
                               "isocheck": [-1], "isoinits": [1], "ts": [10]},
                 datasets=["kbs/kinships"],
                 templates=["template_embeddings"],
                 walltime="10:00:00",
                 memory_max="20g",
                 rci=True,
                 template_per_dataset=True,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="lossless_kbc",
                 param_ranges={"iso": [-1, 14], "prune": [-1, 1], "opt": ["adam"], "lr": [0.01],
                               "xval": [5], "ts": [1000]},
                 datasets="kbs",
                 templates=["template_embeddings"],
                 walltime="23:59:00",
                 memory_max="30g",
                 rci=True,
                 template_per_dataset=True,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="lossless_lrnn",
                 param_ranges={"iso": [-1, 14], "prune": [-1, 1], "opt": ["adam"], "lr": [0.01],
                               "xval": [5], "ts": [1000]},
                 datasets="molecules",
                 templates=["molecules/LRNN_template_embeddings"],
                 walltime="23:59:00",
                 memory_max="30g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="lossless_gnn",
                 param_ranges={"iso": [-1, 14], "prune": [-1, 1], "opt": ["adam"], "lr": [0.01],
                               "xval": [5], "ts": [1000]},
                 datasets="molecules",
                 templates=["molecules/GNN_template_embeddings"],
                 walltime="23:59:00",
                 memory_max="30g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="digits_lrnn_scalar",
                 param_ranges={"iso": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "prune": [1], "xval": [5],
                               "isocheck": [-1], "isoinits": [1], "opt": ["adam"], "lr": [0.01], "ts": [1000]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/scalar_template_embeddings"],
                 walltime="23:59:00",
                 memory_max="40g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

#%%

grid = GridSetup(experiment_id="lrnn_scalar",
                 param_ranges={"iso": [-1], "prune": [-1], "opt": ["adam"], "lr": [0.01],
                               "xval": [5], "ts": [1000]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/scalar_template_embeddings"],
                 walltime="23:59:00",
                 memory_max="80g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

# %%

grid = GridSetup(experiment_id="digits_lrnn_scalar_inits",
                 param_ranges={"iso": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "prune": [1], "xval": [5],
                               "isocheck": [1], "isoinits": [1, 2, 3], "ts": [10]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/scalar_template_embeddings"],
                 walltime="20:00:00",
                 memory_max="40g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)

#%%

grid = GridSetup(experiment_id="digits_lrnn_vector",
                 param_ranges={"iso": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "prune": [1], "xval": [5],
                               "isocheck": [1], "isoinits": [1, 2, 3], "ts": [10]},
                 datasets=["molecules/MDA_MB_231_ATCC"],
                 templates=["molecules/LRNN_template_embeddings"],
                 walltime="20:00:00",
                 memory_max="20g",
                 rci=True,
                 template_per_dataset=False,
                 user="XXXXX")

experiments = grid.generate_experiments()
grid.export_experiments(experiments)
