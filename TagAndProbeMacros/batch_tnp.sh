#!/bin/bash
export X509_USER_PROXY=/afs/cern.ch/user/s/sblancof/.proxy
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/work/s/sblancof/private/Run3Analysis/trigger_2/CMSSW_13_0_5_patch2/src/TagAndProbe_Trigger/TagAndProbeMacros
eval `scramv1 ru -sh`
./tnp_Mu_ZmassUp InputFile_Muon_Run2022E.txt 
