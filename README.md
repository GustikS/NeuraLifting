_This repository contains materials to reproduce the results from the paper "**Lossless Compression of Structured Convolutional Models via Lifting**"._

#### Overview

|  item        | description                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  datasets        |  contains all the datasets. Labels (queries) and evidence (examples) are stored separately (in predicate logic format).                                        |
|  plotting        |  contains python scripts for drawing graphs from the paper                                                                                                     |
|  results         |  contains detailed statistics exported by the learning engine in JSON format for each experiment (prefilled with a rerun). Also includes the generated images. |
|  scripts         |  contains bash scripts for running all the experiments, i.e. running the learning engine with varying inputs and parameters                                    |
|  templates       |  contains all the used templates (models) for learning in the experiments    

- for you convenience, the whole learning engine is packed into a single [jar file release](https://github.com/GustikS/NeuraLifting/releases) with no dependencies (but Java >= 1.8). See the [NeuraLogic](https://github.com/GustikS/NeuraLogic) repository for sourcecode of the engine itself (and recent releases).
- for the comparison against GNN engines (PyG and DGL) from Table 1 (and other experiments), please see a separate [GNNs vs. LRNNs](https://github.com/GustikS/GNNwLRNNs) repository.

#### Reproduction scripts

Since there are many experiments to be performed for the final graphical output, we have prepared [batch run scripts](./scripts) for a convenient run in a cluster environment. If you have access to some computer cluster with the commonly used [SLURM](https://slurm.schedmd.com/quickstart.html) workload manager, you can rerun everything in under 5 minutes of setup. 

- If you cannot run on a cluster, or want to rerun only selected experiments, you can always run [particular shell scripts](./scripts/digits_gnn/scripts/molecules_MDA_MB_231_ATCC_molecules_GNN_template_embeddings__-iso_1_-prune_1_-xval_5_-isocheck_-1_-isoinits_1_-ts_10.sh) with particular parameter setups individually. 
    - Also, you can browse the detailed JSON results individually/manually. 
- We also include a [runscript generator](./plotting/regenerate_run_scripts%20(optional).py) if you wish to test other parammeter setups conveniently.

##### Step by step


1. copy this folder into you home directory at the cluster:

    `sftp://XXXXX@login.HOSTNAME/home/XXXXX`

2. replace 'XXXXX' string by your username in ALL the scripts (using e.g. sed/grep)

    `find ./ -type f -exec sed -i -e 's/XXXXX/USERNAME/g' {} \;`

3. run the grid batch script file in each experiment batch (`EXPERIMENT_BATCH`) directory :

    `bash scripts/EXPERIMENT_BATCH/scripts/200__grid.sh`

4. wait for all the experiments to finish (mostly minutes, but some, particularly the uncompressed scalar models, can take many hours). Be aware that experiments with the uncompressed templates may also consume a lot of memory. 
    1. Consequently, result folders containing all the detailed information from each experiment will show up in the JSON format (in the `./results` folder).

5. automatically load the json data to plot the Figures from the paper using the enclosed [python scripts](./plotting)
    1. for these you'll need basic python libraries such as json, pandas and matplotlib.
    1. To switch between the subplots of each figure, please uncomment the corresponding lines (also for the legend to show in the last plot please uncomment the corresponding line).

    `python ./plotting/figure5.py`