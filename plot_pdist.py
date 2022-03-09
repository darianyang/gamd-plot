"""
Python code to plot just a 2D standard probability distrubution.
The data should be formatted in 2 columns.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_pre_rw_pdist(file):
    """
    Parameters
    ----------
    file : str
        Name of the data file.
    """

    data = np.loadtxt(file)
    print(np.shape(data[::10,0]))
    Z, xedges, yedges = np.histogram2d(data[::10,0], data[::10,1], bins=100)
    # normalize the pdist (-ln(P/P(max)))
    Z = -np.log(np.divide(Z, np.max(Z)))
    plt.figure(figsize=(5,4))
    plt.pcolormesh(xedges, yedges, Z.T)
    cbar = plt.colorbar()
    plt.clim(vmin=0, vmax=4)
    cbar.set_label("-ln P(x)")

    plt.title("2KOD GaMD - 200ns")
    plt.xlim(20,90)
    plt.xlabel("Helical Angle (°)")
    plt.ylim(3,8)
    plt.ylabel("RMSD to Alt PDB ($\AA$)")

    #plt.show()
    plt.savefig("/Users/darian/Desktop/gamd.png")


plot_pre_rw_pdist("data/c2_xrms.tsv")