#!/bin/bash

# MC: perform Maclaurin Series reweighting of GaMD data (equivalent to 1st order CE)
# CE: 2nd order cumulant expansion reweighting
# args : Emax (kcal/mol), cutoff (min n configs in a hist bin), binx, biny, data, T
# disc is the bin discretization interval
# python ../py_reweighting/PyReweighting-2D.py -input agg_oas.dat -T 298 -Emax 15 -cutoff 10 -discX 0.75 -Xdim 0 75 -discY 0.75 -Ydim 0 75 -job amdweight_CE -weight agg_2kod_weights.dat

# for tt and c2
python ../py_reweighting/PyReweighting-2D.py -input agg_tt_c2.dat -T 298 -Emax 15 -cutoff 10 -discX 0.75 -Xdim 0 75 -discY 0.75 -Ydim 0 75 -job amdweight_CE -weight agg_2kod_weights.dat