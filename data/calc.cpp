    parm m01_2kod_gamd_dry.prmtop 
 trajin 06_gamd_prod_dry.nc 1 198000 1 
 reference /ihome/lchong/dty7/bgfs-dty7/hiv1_capsid/std/1a43/hi_pH/v00/02_min.pdb name <xtal> 
 reference /ihome/lchong/dty7/bgfs-dty7/hiv1_capsid/std/2kod/hi_pH/v00/02_min.pdb name <nmr> 
 rms XREF_RMS :1-75,94-163&!@H= out XTAL_REF_RMS_Heavy.dat ref <xtal> mass 
 rms NMR_RMS :1-75,94-163&!@H= out NMR_REF_RMS_Heavy.dat ref <nmr> mass 
 # calc dimer C2 helical angle 
 vector D1 :1-75@CA,C,O,N :39@CA,C,O,N 
 vector D2 :89-163@CA,C,O,N :127@CA,C,O,N 
 vectormath vec1 D1 vec2 D2 out 1-75_39_c2_angle.dat name C2_Angle dotangle 
 # calc distance between (COM) both O eps of E175 and H eps 1 of W184 
 distance M1-E175-Oe_M2-W184-He1 :32@OE1,OE2 :129@HE1 out M1-Oe_M2-He1.dat 
 distance M2-E175-Oe_M1-W184-He1 :120@OE1,OE2 :41@HE1 out M2-Oe_M1-He1.dat 
 run 
 quit
