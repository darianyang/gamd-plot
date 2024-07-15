
import matplotlib.pyplot as plt
import mdap

#oa_names = [f"data/1a43/v0{i}/200ns/o_angle.dat" for i in range(0,5)]
oa_names = [f"data/2kod/v0{i}/200ns/o_angle.dat" for i in range(0,5)]

plotter = mdap.MD_Plot(Xname=oa_names, Xindex=1, Yname=oa_names, Yindex=2, data_type="pdist").plot()
plt.xlim(0,75)
plt.ylim(0,75)

plt.show()
