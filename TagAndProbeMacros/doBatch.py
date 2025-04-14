import subprocess
import subprocess
from pathlib import Path
from math import ceil
import os

datasets = ["DY_Electron"] # "Muon", "EGamma", "DY_Muon"
years = ["Run2024"]

base_sh = """
#!/bin/bash                                                                                                                                                                                                
export X509_USER_PROXY=/afs/cern.ch/user/s/sblancof/.proxy
voms-proxy-info
export SCRAM_ARCH=el8_amd64_gcc12
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/work/s/sblancof/private/Run3Analysis/trigger_2/CMSSW_15_0_2/src/TagAndProbe_Trigger/TagAndProbeMacros
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
requirements = (OpSysAndVer =?= "AlmaLinux9")
MY.SingularityImage = "/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/batch-team/containers/plusbatch/el8-full:latest"
queue 1 Folder in RPLME_FOLDER 
"""

# ./tnp_Mu_ZmassUp InputFile_Muon_Run2022E.txt

folder = []
inputs_to_transfer = []

for year in years:
    for dataset in datasets:

        inFile = "InputFile_"+dataset+"_"+year+".txt"
        inputs_to_transfer.append(inFile)

        num_lines = sum(1 for _ in open(inFile))
        chunksize = 10
        nIterations = max(ceil(num_lines / chunksize), 1)

        if dataset == "Muon":
            executable = ["tnp_mu_Run2024"]
        elif dataset == "EGamma":
            executable = ["tnp_ele_Run2024"]
        elif dataset == "DY_Electron":
            executable = ["tnp_DY_ele_Run2024"]
        elif dataset == "DY_Muon":
            executable = ["tnp_DY_mu_Run2024"]        

        for execs in executable:
            
            for i in range(nIterations):

                #execs = execs + "_" + year.split("Run")[1]            
                script_sh = base_sh + "\n"
                for j in range(chunksize):
                    script_sh += f"./{execs} {inFile} rootFiles/iteration{i}/file{j}_ {i*chunksize + j} \n"
                
                tag = execs.split("tnp_")[1]
                Path(f'condor/{tag}_iteration{i}').mkdir(parents=True, exist_ok=True)
                Path(f"rootFiles/iteration{i}").mkdir(parents=True, exist_ok=True)
                folder.append(f"{tag}_iteration{i}")
                
                with open(f"condor/{tag}_iteration{i}/script.sh", "w") as file:
                    file.write(script_sh)
                    
                process = subprocess.Popen(
                    f"chmod +x condor/{tag}_iteration{i}/script.sh", shell=True
                )
                process.wait()


base_jds = base_jds.replace("RPLME_INPUTS", ",".join(inputs_to_transfer))
base_jds = base_jds.replace("RPLME_FOLDER", ", ".join(folder))

with open("condor_submit.jds", "w") as file:
    file.write(base_jds)
                
