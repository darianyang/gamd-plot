"""
Load in and format the weight files for all 5 replicates into a single file.
"""

import numpy as np

# frames of 5 reps, 3 cols: 
# Column 1: dV in units of kbT; column 2: timestep; column 3: dV in units of kcal/mol
frames = 200000
agg_weights = np.zeros((frames*5, 3))

weight_files = [f"data-2kod/v0{i}/weights.dat" for i in range(0,5)]

#w = np.loadtxt("data-2kod/v00/weights.dat")
#w[:,1] += 101000000
#print(w)

for i in range(0,5):
    # load in the 3 col weight data
    w_data = np.loadtxt(f"data-2kod/v0{i}/weights.dat")
    # adjust timestep col for each replicate
    w_data[:,1] += 101000000 * i
    # fill in the agg array
    agg_weights[frames*i:frames*(i+1)] = w_data

np.savetxt("data-2kod/agg_2kod_weights.dat", agg_weights)