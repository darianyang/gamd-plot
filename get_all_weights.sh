#!/bin/bash
# grab weights for all 5 replicates


for VER in $(seq -f "%02g" 0 1 4) ; do
    tail -n +5 data-2kod/v${VER}//200ns/gamd.log | awk 'NR%1==0' | awk '{print ($8+$7)/(0.001987*298)"                " $2  "             " ($8+$7)}' > data-2kod/v${VER}/weights.dat
done

