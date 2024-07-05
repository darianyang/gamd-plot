"""
Python code to plot just a 2D standard probability distrubution.
The data should be formatted in 2 columns.
"""

import numpy as np
import matplotlib.pyplot as plt

def pre_processing(file=None, data=None, time_units=10**6, index=1):
    """
    Processes raw time series data to appropriate units of time.
    """
    if file:
        dstacked = np.array([])
        # multi file list
        for f in file:
            data = np.genfromtxt(f)
            dstacked = np.concatenate((dstacked, data[:,index]), axis=0)
    # time units should mostly be in ps: convert to us
    #time = np.divide(data[:,0], time_units)
    #return np.vstack([time, data[:,index]])
    return dstacked

def plot_pre_rw_pdist(data_x, data_y):
    """
    Parameters
    ----------
    file : str
        Name of the data file.
    """
    # data_x = np.array(data_x)
    # data_y = np.array(data_y)
    Z, xedges, yedges = np.histogram2d(data_x, data_y, bins=100)
    # normalize the pdist (-ln(P/P(max)))
    Z = -np.log(np.divide(Z, np.max(Z)))
    plt.figure(figsize=(5,4))
    plt.pcolormesh(xedges, yedges, Z.T)
    cbar = plt.colorbar()
    plt.clim(vmin=0, vmax=5)
    cbar.set_label("-ln P(x)")

    plt.title("2KOD GaMD (1$\mu$s)")
    plt.ylim(20, 100)
    plt.ylabel("C2 Angle (°)")
    plt.xlim(0, 80)
    plt.xlabel("Orientation Angle (°)")

    #plt.show()
    plt.tight_layout()
    #plt.savefig("/Users/darian/Desktop/200ns-gamd.png", dpi=300, transparent=True)


# plot_pre_rw_pdist("data/c2_xrms.tsv")
plot_pre_rw_pdist(pre_processing([f"data/2kod/v0{i}/200ns/o_angle.dat" for i in range(0,5)]),
                  pre_processing([f"data/2kod/v0{i}/200ns/1-75_39_c2_angle.dat" for i in range(0,5)])
                  )

plt.show()