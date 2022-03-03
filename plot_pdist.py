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
    Z, xedges, yedges = np.histogram2d(data[:,0], data[:,1], bins=100)
    # normalize the pdist (-ln(P/P(max)))
    Z = -np.log(np.divide(Z, np.max(Z)))
    plt.pcolormesh(xedges, yedges, Z.T)
    plt.colorbar()
    plt.show()


plot_pre_rw_pdist("data/c2_xrms.tsv")