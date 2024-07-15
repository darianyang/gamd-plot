#!/bin/bash

# perform Maclaurin Series reweighting of GaMD data (eqivalent to 1st order CE)
# args : Emax (kcal/mol), cutoff (min n configs in a hist bin), binx, biny, data, T
# disc is the bin discretization interval
python ../py_reweighting/PyReweighting-2D.py -input agg_oas.dat -T 298 -Emax 30 -cutoff 10 -discX 0.75 -Xdim 0 75 -discY 0.75 -Ydim 0 75 -job amdweight_MC -weight agg_weights.dat