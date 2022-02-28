# Test of GaMD using input scripts from Sztain 2021 JCIM
# https://github.com/tsztain/SARS-CoV-2_protease_GaMD/tree/master/Trajectory_inputs

* the starting state will be the equilibrated state from standard MD
* or I can start a new equil process?
    * well I can at least test with the previously equilibrated data

* got 05_equil files for 2kod from hi_pH v00 or m01
* documented Terra's gamd input file 06_gamd.in
* ran a test run using a new file with Chong lab NPT conditions
    * gamd_test.in
    * this will generate 200ns of data (mostly GaMD)
