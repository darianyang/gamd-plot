#!/bin/bash
# process and analyze gamd output data
# calculate data and reweight

CPPTRAJ=cpptraj

NMR_REF=data/02_min_nmr.pdb
XTAL_REF=data/02_min_xtal.pdb

if [ $1 = "calc" ] ; then
    # calc datasets of interest
    C0="    parm data/m01_2kod_gamd_dry.prmtop \n"
    C0="$C0 trajin data/06_gamd_prod_dry.nc 1 198000 1 \n"
    C0="$C0 reference $XTAL_REF name <xtal> \n"
    C0="$C0 reference $NMR_REF name <nmr> \n"
    C0="$C0 rms XREF_RMS :1-75,94-163&!@H= out data/XTAL_REF_RMS_Heavy.dat ref <xtal> mass \n"
    C0="$C0 rms NMR_RMS :1-75,94-163&!@H= out data/NMR_REF_RMS_Heavy.dat ref <nmr> mass \n"
    C0="$C0 # calc dimer C2 helical angle \n"
    C0="$C0 vector D1 :1-75@CA,C,O,N :39@CA,C,O,N \n"
    C0="$C0 vector D2 :89-163@CA,C,O,N :127@CA,C,O,N \n"
    C0="$C0 vectormath vec1 D1 vec2 D2 out data/1-75_39_c2_angle.dat name C2_Angle dotangle \n"
    C0="$C0 # calc distance between (COM) both O eps of E175 and H eps 1 of W184 \n"
    C0="$C0 distance M1-E175-Oe_M2-W184-He1 :32@OE1,OE2 :129@HE1 out data/M1-Oe_M2-He1.dat \n"
    C0="$C0 distance M2-E175-Oe_M1-W184-He1 :120@OE1,OE2 :41@HE1 out data/M2-Oe_M1-He1.dat \n"
    C0="$C0 run \n"
    C0="$C0 quit"
    
    echo -e "$C0" > data/calc.cpp
    #$DO_PARALLEL \
    $CPPTRAJ -i data/calc.cpp > data/calc.cpp.out

elif [ $1 = "prep" ] ; then
    # make clean data files for reweighting
    cat data/XTAL_REF_RMS_Heavy.dat | tail -n +2 | awk {'print $2'} > data/xrms.dat
    cat data/1-75_39_c2_angle.dat | tail -n +2 | awk {'print $2'} > data/c2.dat
    # make 2D data file tsv
    paste data/xrms.dat data/c2.dat | column -s $'\t' -t > data/xrms_c2.tsv
    paste data/c2.dat data/xrms.dat | column -s $'\t' -t > data/c2_xrms.tsv
    
    # NOTE: weights and data files must be same size
    # make weights file from gamd log file
    # Prepare input file "weights.dat" in the following format:
    # Column 1: dV in units of kbT; column 2: timestep; column 3: dV in units of kcal/mol 
    #nlines=198000 # number of data points used for reweighting
    #tail -n $nlines gamd.log | awk 'NR%1==0' | awk '{print ($8+$7)/(0.001987*298)"                " $2  "             " ($8+$7)}' > weights.dat
    tail -n +5 data/gamd.log | awk 'NR%1==0' | awk '{print ($8+$7)/(0.001987*298)"                " $2  "             " ($8+$7)}' > data/weights.dat

elif [ $1 = "rw" ] ; then
    cd data
    # perform reweighting of GaMD data
    # args : Emax (kcal/mol), cutoff (kcal/mol), binx, biny, data, T
    #bash py_reweighting/reweight-2d.sh 100 100 6 6 c2_xrms.tsv 298
    python3 ../py_reweighting/PyReweighting-2D.py -input c2_xrms.tsv -T 298 -Emax 10 -cutoff 10 -discX 0.5 -Xdim 20 80 -discY 0.05 -Ydim 2 9 -job amdweight_MC -weight weights.dat
    # TODO: add args for xlabel and ylabel

else
    echo "ARG 1 MUST BE 'calc', 'prep', or 'rw'"
fi
