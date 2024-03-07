import subprocess


#Indir = "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_EGamma_2022EReReco/EGamma/Run2022E/240112_090304/0000/"
#Indir = "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022EReReco/Muon/Run2022E/240112_090313/0000/"

#Indirs = ["/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/Muon/Run2022C2/231027_141355/0000/",
#         "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/Muon/Run2022D/231027_141349/0000/",
#         "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/SingleMuon/Run2022B/231027_141407/0000/",
#         "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/SingleMuon/Run2022C1/231027_141401/0000/"]

#Indirs = ["/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_EGamma_2022ReReco/EGamma/Run2022B/231027_141238/0000/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_EGamma_2022ReReco/EGamma/Run2022C/231027_141231/0000/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_EGamma_2022ReReco/EGamma/Run2022D/231027_141224/0000/"]


#Indirs = ["/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0000/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0001/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0002/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0003/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0004/",
#          "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022EEPrompt/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L/230724_111055/0005/"
#]

Indirs = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_DYtoLL_2022ReReco/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/DYto2L/240119_110507/0000/"
]

#Indirs = [
#    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/SingleMuon/Run2022B/240119_110327/0000/",
#    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/SingleMuon/Run2022C1/240119_110322/0000/",
#    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/Muon/Run2022C2/240119_110316/0000/",
#    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco/Muon/Run2022D/240119_110312/0000/"
#]

fnames_tot = []

for Indir in Indirs:
    print("------------------------")
    print(Indir)
    cmd = ("find {} -name '*.root'").format(Indir)
    fnames = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames = [fname_tmp.decode('ascii') for fname_tmp in fnames]
    fnames_tot += fnames

f = open("InputFile_DY_Run2022BCD.txt", "w")

for fname in fnames_tot:
    f.write(fname)
    f.write("\n")

f.close()




