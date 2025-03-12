import subprocess

Indirs = {}

####### 2022 (Early)

# EGamma

Indirs['EGamma_Run2022'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2022/EGamma/Run2022C/240618_133023/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2022/EGamma/Run2022D/240618_133019/0000",
]

# Muon

Indirs['Muon_Run2022'] = [ 
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/SingleMuon/Run2022C1/240618_140041/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/Muon/Run2022C2/240618_140037/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/Muon/Run2022D/240618_140033/0000",
]

# MC

Indirs['DY_Run2022'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22/240618_140124/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22/240618_140124/0001",
]

###### 2022EE (Late)

# EGamma

Indirs['EGamma_Run2022EE'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2022/EGamma/Run2022E/240618_133014/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2022/EGamma/Run2022F/240618_133009/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2022/EGamma/Run2022G/240618_133425/0000",
]

# Muon

Indirs['Muon_Run2022EE'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/Muon/Run2022E/240618_140029/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/Muon/Run2022F/240618_140025/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2022/Muon/Run2022G/240618_140021/0000",
]

# MC

Indirs['DY_Run2022EE'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22EE/240618_140120/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22EE/240618_140120/0001",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22EE/240618_140120/0002",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2022/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_22EE/240618_140120/0003",
]

###### 2023 (Early)

# EGamma

Indirs['EGamma_Run2023'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023C_0v1/240618_142657/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023C_0v2/240618_142652/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023C_0v3/240618_142648/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023C_0v4/240618_142644/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023C_1v1/240618_142641/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023C_1v2/240618_142637/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023C_1v3/240618_142633/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023C_1v4/240618_142629/0000",
]

# Muon

Indirs['Muon_Run2023'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023C_0v1/240618_142829/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023C_0v2/240618_142826/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023C_0v3/240618_142822/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023C_0v4/240618_142818/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023C_1v1/240618_142814/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023C_1v2/240618_142811/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023C_1v3/240618_142807/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023C_1v4/240618_142803/0000",
]

# MC

Indirs['DY_Run2023'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2023/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_23/240618_142851/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2023/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_23/240618_142851/0001",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2023/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_23/240618_142851/0002",
]

####### 2023BPix (Late)

# EGamma

Indirs['EGamma_Run2023BPix'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023D_0v1/240618_142625/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma0/Run2023D_0v2/240618_142621/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023D_1v1/240618_142617/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2023/EGamma1/Run2023D_1v2/240618_142613/0000",
]

# Muon

Indirs['Muon_Run2023BPix'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023D_0v1/240618_142759/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon0/Run2023D_0v2/240618_142756/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023D_1v1/240618_142752/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023/Muon1/Run2023D_1v2/240618_142748/0000",
]

# MC

Indirs['DY_Run2023BPix'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2023/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_23BPix/240618_142848/0000",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYtoLL_2023/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2L_23BPix/240618_142848/0001",
]


for key in Indirs:

    fnames_tot = []

    for Indir in Indirs[key]:
        print("------------------------")
        print(Indir)
        cmd = ("find {} -name '*.root'").format(Indir)
        fnames = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
        fnames = [fname_tmp.decode('ascii') for fname_tmp in fnames]
        fnames_tot += fnames

    f = open(f"InputFile_{key}.txt", "w")
    
    for fname in fnames_tot:
        f.write(fname)
        f.write("\n")
    
    f.close()




