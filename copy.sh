#!/bin/bash
# copy.sh

SYSTEMS=(hi_pH)
FF="data-2kod"
OUT_ROOT=200ns
SOURCE=/home/dty7/DTY-H2P/h2p/hiv1_capsid/gamd/2kod

for SYS in ${SYSTEMS[@]} ; do
    mkdir -p $FF
    cd $FF
    for VER in $(seq -f "%02g" 0 1 4) ; do
        mkdir -p v$VER/$OUT_ROOT
        rsync -axvhP $SOURCE/$SYS/v$VER/06_gamd.in v$VER/$OUT_ROOT/
    done
    cd ../
done

#SYSTEMS=(2kod 1a43)
#FF="data"
#OUT_ROOT=200ns
#SOURCE=/bgfs/lchong/dty7/hiv1_capsid/gamd
#
#for SYS in ${SYSTEMS[@]} ; do
#    mkdir -p $FF/$SYS
#    cd $FF/$SYS
#    for VER in $(seq -f "%02g" 0 1 4) ; do
#        mkdir -p v$VER/$OUT_ROOT
#        rsync -axhvP dty7@h2p.crc.pitt.edu:$SOURCE/$SYS/hi_pH/v$VER/$OUT_ROOT/*.dat v$VER/$OUT_ROOT/
#    done
#    cd ../..
#done
