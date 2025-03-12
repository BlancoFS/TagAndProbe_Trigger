import subprocess
import subprocess
from pathlib import Path
import os

datasets = ["Muon", "EGamma", "DY"]
years = ["Run2022", "Run2022EE", "Run2023", "Run2023BPix"]


base_sh = """
#!/bin/bash                                                                                                                                                                                                                                                                    
export X509_USER_PROXY=/afs/cern.ch/user/s/sblancof/.proxy
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/work/s/sblancof/private/Run3Analysis/trigger_2/CMSSW_13_0_5_patch2/src/TagAndProbe_Trigger/TagAndProbeMacros
eval `scramv1 ru -sh`
"""

base_jds = """
universe    = vanilla
executable  = condor/$(Folder)/script.sh
transfer_input_files = RPLME_INPUTS
output      = /dev/null
error       = /dev/null
log         = /dev/null
+JobFlavour = "testmatch"
MY.WantOS = "el8"
requirements = (OpSysAndVer =?= "AlmaLinux9")
queue 1 Folder in RPLME_FOLDER 
"""

# ./tnp_Mu_ZmassUp InputFile_Muon_Run2022E.txt

folder = []
inputs_to_transfer = []

for year in years:
    for dataset in datasets:

        inFile = "InputFile_"+dataset+"_"+year+".txt"
        inputs_to_transfer.append(inFile)
        
        if dataset == "Muon":
            executable = ["tnp_Mu"]
        elif dataset == "EGamma":
            executable = ["tnp_Ele"]
        elif dataset == "DY":
            executable = ["tnp_DY_Ele", "tnp_DY_Mu"]

        for execs in executable:
            
            execs = execs + "_" + year.split("Run")[1]
            script_sh = base_sh + "\n"
            script_sh += f"./{execs} {inFile}"
            
            tag = execs.split("tnp_")[1]            
            Path(f'condor/{tag}').mkdir(parents=True, exist_ok=True)
            folder.append(tag)

            with open(f"condor/{tag}/script.sh", "w") as file:
                file.write(script_sh)

            process = subprocess.Popen(
                f"chmod +x condor/{tag}/script.sh", shell=True
            )
            process.wait()


base_jds = base_jds.replace("RPLME_INPUTS", ",".join(inputs_to_transfer))
base_jds = base_jds.replace("RPLME_FOLDER", ", ".join(folder))

with open("condor_submit.jds", "w") as file:
    file.write(base_jds)
                
