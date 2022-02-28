#!/bin/bash
# process and analyze gamd output data
# calculate data and reweight

T=298
CPPTRAJ=cpptraj

NMR_REF=/ihome/lchong/dty7/bgfs-dty7/hiv1_capsid/std/2kod/hi_pH/v00/02_min.pdb
XTAL_REF=/ihome/lchong/dty7/bgfs-dty7/hiv1_capsid/std/1a43/hi_pH/v00/02_min.pdb

if [ $1 = "calc" ] ; then
    # calc datasets of interest
    C0="    parm m01_2kod_gamd_dry.prmtop \n"
    C0="$C0 trajin 06_gamd_prod_dry.nc 1 198000 1 \n"
    C0="$C0 reference $XTAL_REF name <xtal> \n"
    C0="$C0 reference $NMR_REF name <nmr> \n"
    C0="$C0 rms XREF_RMS :1-75,94-163&!@H= out XTAL_REF_RMS_Heavy.dat ref <xtal> mass \n"
    C0="$C0 rms NMR_RMS :1-75,94-163&!@H= out NMR_REF_RMS_Heavy.dat ref <nmr> mass \n"
    C0="$C0 # calc dimer C2 helical angle \n"
    C0="$C0 vector D1 :1-75@CA,C,O,N :39@CA,C,O,N \n"
    C0="$C0 vector D2 :89-163@CA,C,O,N :127@CA,C,O,N \n"
    C0="$C0 vectormath vec1 D1 vec2 D2 out 1-75_39_c2_angle.dat name C2_Angle dotangle \n"
    C0="$C0 # calc distance between (COM) both O eps of E175 and H eps 1 of W184 \n"
    C0="$C0 distance M1-E175-Oe_M2-W184-He1 :32@OE1,OE2 :129@HE1 out M1-Oe_M2-He1.dat \n"
    C0="$C0 distance M2-E175-Oe_M1-W184-He1 :120@OE1,OE2 :41@HE1 out M2-Oe_M1-He1.dat \n"
    C0="$C0 run \n"
    C0="$C0 quit"
    
    echo -e "$C0" > calc.cpp
    #$DO_PARALLEL \
    $CPPTRAJ -i calc.cpp > calc.cpp.out &&

elif [ $1 = "prep" ] ; then
    # make clean data files for reweighting
    cat XTAL_REF_RMS_Heavy.dat | tail -n +2 | awk {'print $2'} > xrms.dat
    cat 1-75_39_c2_angle.dat | tail -n +2 | awk {'print $2'} > c2.dat
    # make 2D data file tsv
    paste xrms.dat c2.dat | column -s $'\t' -t > xrms_c2.tsv
    paste c2.dat xrms.dat | column -s $'\t' -t > c2_xrms.tsv
    
    # NOTE: weights and data files must be same size
    # make weights file from gamd log file
    # Prepare input file "weights.dat" in the following format:
    # Column 1: dV in units of kbT; column 2: timestep; column 3: dV in units of kcal/mol 
    #nlines=198000 # number of data points used for reweighting
    #tail -n $nlines gamd.log | awk 'NR%1==0' | awk '{print ($8+$7)/(0.001987*298)"                " $2  "             " ($8+$7)}' > weights.dat
    tail -n +5 gamd.log | awk 'NR%1==0' | awk '{print ($8+$7)/(0.001987*298)"                " $2  "             " ($8+$7)}' > weights.dat

elif [ $1 = "rw" ] ; then
    # perform reweighting of GaMD data
    # args : Emax (kcal/mol), cutoff (kcal/mol), binx, biny, data, T, TODO:xdim, ydim
    bash py_reweighting/reweight-2d.sh 100 100 6 6 c2_xrms.tsv $T

else
    echo "ARG 1 MUST BE 'calc', 'prep', or 'rw'"
fi
