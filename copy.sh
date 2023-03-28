#!/bin/bash
# copy.sh

SYSTEMS=(2kod 1a43)
FF="data"
OUT_ROOT=200ns
SOURCE=/bgfs/lchong/dty7/hiv1_capsid/gamd

for SYS in ${SYSTEMS[@]} ; do
    mkdir -p $FF/$SYS
    cd $FF/$SYS
    for VER in $(seq -f "%02g" 0 1 4) ; do
        mkdir -p v$VER/$OUT_ROOT
        rsync -axhvP dty7@h2p.crc.pitt.edu:$SOURCE/$SYS/hi_pH/v$VER/$OUT_ROOT/*.dat v$VER/$OUT_ROOT/
    done
    cd ../..
done
