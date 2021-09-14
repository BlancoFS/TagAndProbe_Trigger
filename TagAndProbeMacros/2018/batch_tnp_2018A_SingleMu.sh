#!/bin/bash
CMACRO="TagAndProbe_Ele.C"  # TagAndProbe_Ele.C or TagAndProbe_Mu.C
EXEC="tnp"
cd /afs/cern.ch/work/a/arun/Latinos/TriggerEff/UL2018/CMSSW_10_6_18/src/TagAndProbe_Trigger/TagAndProbeMacros/2018
#eval `scramv1 runtime -csh`
#g++ Run_TnP.cxx -o $EXEC  -std=c++0x `root-config --libs --cflags` -include $CMACRO
g++ Run_TnP.cxx -o tnp_Mu2018A -std=c++0x `root-config --libs --cflags` -include TagAndProbe_Mu2018A.C 
./tnp_Mu2018A list_2018A_Muon.txt  efficiency