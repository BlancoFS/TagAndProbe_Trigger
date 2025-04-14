import subprocess

Indirs = {}

"""
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

######## 2024

# EGamma

Indirs['EGamma_Run2024'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024C_EGamma0/250408_114220/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024D_EGamma0/250408_114210/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024E_EGamma0/250408_114157/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024F_EGamma0/250408_114146/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024G_EGamma0/250408_114134/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024H_EGamma0/250408_114120/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024Iv1_EGamma0/250408_114109/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma0/Run2024Iv2_EGamma0/250408_114058/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024C_EGamma1/250408_114215/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024D_EGamma1/250408_114202/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024E_EGamma1/250408_114152/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024F_EGamma1/250408_114140/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024G_EGamma1/250408_114127/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024H_EGamma1/250408_114115/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024Iv1_EGamma1/250408_114103/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_EGamma_2024/EGamma1/Run2024Iv2_EGamma1/250408_114051/0000/",
]
    
# Muon

Indirs['Muon_Run2024'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024C_Muon0/250408_113926/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024D_Muon0/250408_113913/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024E_Muon0/250408_113902/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024F_Muon0/250408_113851/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024G_Muon0/250408_113841/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024H_Muon0/250408_113830/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024Iv1_Muon0/250408_113819/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon0/Run2024Iv2_Muon0/250408_113809/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024C_Muon1/250408_113920/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024D_Muon1/250408_113908/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024E_Muon1/250408_113856/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024F_Muon1/250408_113846/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024G_Muon1/250408_113835/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024H_Muon1/250408_113825/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024Iv1_Muon1/250408_113814/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2024/Muon1/Run2024Iv2_Muon1/250408_113803/0000/",
]

# MC

Indirs['DY_Muon_Run2024'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0000/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0001/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0002/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0003/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0004/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0005/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0006/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0007/",
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2Mu_24/250408_114311/0008/",
]

"""

Indirs['DY_Electron_Run2024'] = [
    "/eos/cms/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2E_2024/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/DYto2E_24/250409_072355/0000/"
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




