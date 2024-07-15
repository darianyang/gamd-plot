
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("~/github/wedap/wedap/styles/default.mplstyle")

fig, ax = plt.subplots()

def plot_pdist(x, y, hist):
    x = np.loadtxt(x)
    y = np.loadtxt(y)
    hist = np.loadtxt(hist)
    pd = ax.pcolormesh(x,y,hist, vmax=10)
    cbar = plt.colorbar(pd)
    cbar.set_label("PMF [k$_B$T$^{-1}$]")
    ax.set_xlabel("Orientation Angle 1 (°)")
    ax.set_ylabel("Orientation Angle 2 (°)")
    ax.set_yticks([0, 20, 40, 60])
    ax.grid()

    # plot PDBs
    ax.scatter(38.2, 38.2, label="4IPY", marker="P", color="white", s=200, edgecolor="k")
    ax.scatter(29.5, 29.5, label="2KOD", marker="*", color="white", s=300, edgecolor="k")
    ax.scatter(19.9, 19.9, label="1A43", marker="d", color="white", s=125, edgecolor="k")

    plt.legend(frameon=False)

plot_pdist("xedges_amdweight_MC.txt", "yedges_amdweight_MC.txt", "rw_hist_amdweight_MC.txt")
#plot_pdist("xedges_amdweight_CE.txt", "yedges_amdweight_CE.txt", "rw_hist_amdweight_CE.txt")
plt.tight_layout()
plt.savefig("rw_oa.pdf")
plt.show()