
import matplotlib.pyplot as plt
import mdap

# oa plot
# #oa_names = [f"data/1a43/v0{i}/200ns/o_angle.dat" for i in range(0,5)]
# oa_names = [f"data/2kod/v0{i}/200ns/o_angle.dat" for i in range(0,5)]
# plotter = mdap.MD_Plot(Xname=oa_names, Xindex=1, Yname=oa_names, Yindex=2, data_type="pdist").plot()
# plt.xlim(0,75)
# plt.ylim(0,75)

# tt c2 plot
tt_names = [f"data-2kod/v0{i}/200ns/tt_dist.dat" for i in range(0,5)]
c2_names = [f"data-2kod/v0{i}/200ns/c2_angle.dat" for i in range(0,5)]
plotter = mdap.MD_Plot(Xname=tt_names, Xindex=1, Yname=c2_names, Yindex=1, data_type="pdist").plot()
plt.xlim(6,18)
plt.ylim(20,100)


plt.show()
