
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("~/github/wedap/wedap/styles/default.mplstyle")

fig, ax = plt.subplots()

def plot_oa_pdist(x, y, hist):
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

def plot_tt_c2_pdist(x, y, hist):
    x = np.loadtxt(x)
    y = np.loadtxt(y)
    hist = np.loadtxt(hist)
    pd = ax.pcolormesh(x,y,hist, vmax=10)
    cbar = plt.colorbar(pd)
    cbar.set_label("PMF [k$_B$T$^{-1}$]")
    ax.set_xlabel("T188-T188 Distance ($\AA$)")
    ax.set_ylabel("C$_2$ Angle (°)")
    #ax.set_yticks([0, 20, 40, 60])
    ax.grid()
    ax.set_xlim(0,18)
    ax.set_ylim(0,110)

    # plot PDBs
    ax.scatter(15, 49.6, label="4IPY", marker="P", color="white", s=200, edgecolor="k")
    ax.scatter(12.2, 55, label="2KOD", marker="*", color="white", s=300, edgecolor="k")
    ax.scatter(8, 37.2, label="1A43", marker="d", color="white", s=125, edgecolor="k")

    plt.legend(frameon=False, loc="upper left")

#plot_oa_pdist("xedges_amdweight_MC.txt", "yedges_amdweight_MC.txt", "rw_hist_amdweight_MC.txt")
plot_tt_c2_pdist("xedges_amdweight_MC.txt", "yedges_amdweight_MC.txt", "rw_hist_amdweight_MC.txt")
plt.tight_layout()
#plt.savefig("rw_oa.pdf")
plt.savefig("rw_tt_c2.pdf")
plt.show()