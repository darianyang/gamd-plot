"""
Load in and format the data files for all 5 replicates into a single file.
"""

import numpy as np

#print(np.loadtxt(f"data-2kod/v00/200ns/o_angle.dat", usecols=[1,2]).shape)

# frames of 5 reps, 3 cols: 
frames = 200000
agg_data = np.zeros((frames*5, 2))

for i in range(0,5):
    # load in the oa data (cols 1 and 2)
    #data = np.loadtxt(f"data-2kod/v0{i}/200ns/o_angle.dat", usecols=[1,2])
    data1 = np.loadtxt(f"data-2kod/v0{i}/200ns/tt_dist.dat", usecols=1).reshape(-1,1)
    data2 = np.loadtxt(f"data-2kod/v0{i}/200ns/c2_angle.dat", usecols=1).reshape(-1,1)
    data = np.hstack((data1, data2))
    #print(data.shape)
    # forgot to remove the first frame, which was apart of the equil
    # I used frames 2000 to last, but should have used 2001 to last
    # correcting this here
    data = data[1:,:]
    # fill in the agg array
    agg_data[frames*i:frames*(i+1)] = data

#np.savetxt("data-2kod/agg_oas.dat", agg_data)
np.savetxt("data-2kod/agg_tt_c2.dat", agg_data)