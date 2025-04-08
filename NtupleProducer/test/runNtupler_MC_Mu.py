import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("Ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.MessageLogger.cerr.FwkReport.reportEvery = 1

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_mcRun3_2024_realistic_v2','')

#
# Define input data to read
#
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
inputFilesAOD = cms.untracked.vstring(
    'root://cms-xrd-global.cern.ch//store/data/Run2017C/SingleElectron/AOD/12Sep2017-v1/70000/80EF56E5-69A6-E711-AB37-48FD8E2824D7.root',
)    
inputFilesMiniAOD = cms.untracked.vstring(
    "root://cms-xrd-global.cern.ch//store/mc/RunIII2024Summer24MiniAODv6/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/MINIAODSIM/150X_mcRun3_2024_realistic_v1-v4/2540000/00c9ebe8-75bf-412b-86a4-9557dac72010.root"
)

#
# You can list here either AOD or miniAOD files, but not both types mixed
#
useAOD = False 
if useAOD == True :
    inputFiles = inputFilesAOD
    outputFile = "electron_ntuple.root"
    pileupProductName = "addPileupInfo"
    print("AOD input files are used")
else :
    inputFiles = inputFilesMiniAOD
    outputFile = "TnP_ntuple.root"
    pileupProductName = "slimmedAddPileupInfo"
    print("MiniAOD input files are used")
process.source = cms.Source ("PoolSource", fileNames = inputFiles )                             

#
# Set up electron ID (VID framework)
#

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format  to be
# DataFormat.AOD or DataFormat.MiniAOD, as appropriate 
if useAOD == True :
    dataFormat = DataFormat.AOD
else :
    dataFormat = DataFormat.MiniAOD

switchOnVIDElectronIdProducer(process, dataFormat)
# define which IDs we want to produce
my_id_modules = [
    'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Winter22_122X_V1_cff',
    'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_RunIIIWinter22_iso_V1_cff',
    'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_RunIIIWinter22_noIso_V1_cff',    
]

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

#
# Configure the ntupler module
#
process.ntupler = cms.EDAnalyzer('Ntupler',
                                 # The module automatically detects AOD vs miniAOD, so we configure both
                                 #
                                 # Common to all formats objects
                                 #
                                 pileup   = cms.InputTag( pileupProductName ),
                                 rho      = cms.InputTag("fixedGridRhoFastjetAll"),
                                 beamSpot = cms.InputTag('offlineBeamSpot'),
                                 genEventInfoProduct = cms.InputTag('generator'),
                                 #
                                 # Objects specific to AOD format
                                 #
                                 electrons    = cms.InputTag("gedGsfElectrons"),
                                 muons        = cms.InputTag("muons"),
                                 genParticles = cms.InputTag("genParticles"),
                                 vertices     = cms.InputTag("offlinePrimaryVertices"),
                                 conversions  = cms.InputTag('allConversions'),
                                 triggerResultTag     = cms.InputTag("TriggerResults", "", "HLT"),
                                 triggerSummaryTag = cms.InputTag("hltTriggerSummaryAOD", "", "HLT"),
                                 l1EGTag      = cms.InputTag("caloStage2Digis","EGamma","RECO"),
                                 l1MuonTag    = cms.InputTag("gmtStage2Digis","Muon","RECO"),

                                 pathsToSave  = cms.vstring( "HLT_Ele30_WPTight_Gsf_v",
                                                             "HLT_Ele32_WPTight_Gsf_v",
                                                             "HLT_Ele35_WPTight_Gsf_v",
                                                             "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                                                             "HLT_IsoMu24_v",
                                                             "HLT_IsoMu27_v",
                                                             "HLT_Mu50_v",
                                                             "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v",
                                                             "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v",
                                                             "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
                                                             "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                                 ),
                                 filterToMatch= cms.vstring(
                                     # Ele
                                     "hltEle30WPTightGsfTrackIsoFilter",
                                     "hltEle32WPTightGsfTrackIsoFilter",
                                     "hltEle35noerWPTightGsfTrackIsoFilter",
                                     "hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter",
                                     "hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter" ,
                                     "hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter",
                                     "hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter",
                                     # Muon
                                     "hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered",
                                     "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered",
                                     #
                                     #"hltL3fL1sSingleMu22L1f0L2f10QL3Filtered24Q",
                                     #"hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q",
                                     #
                                     "hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q",
                                     "hltL3fL1DoubleMu155fFiltered17",
                                     "hltL3fL1DoubleMu155fPreFiltered8",
                                     #
                                     "hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered8",
                                     "hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23",
                                     #"hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL1Filtered0",
                                     #"hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL1Filtered0",
                                 ),
				 HLTprocess = cms.string("HLT"),
				 #
                                 # Objects specific to MiniAOD format
                                 #
                                 electronsMiniAOD    = cms.InputTag("slimmedElectrons"),
                                 genParticlesMiniAOD = cms.InputTag("prunedGenParticles"),
                                 verticesMiniAOD     = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                 conversionsMiniAOD  = cms.InputTag('reducedEgamma:reducedConversions'),
                                 muonsMiniAOD = cms.InputTag("slimmedMuons"),
                                 trigger     = cms.InputTag("TriggerResults", "", "HLT"),
			         prescale = cms.InputTag("patTrigger"),
                                 objects = cms.InputTag('slimmedPatTrigger'),
                                 # Effective areas for computing PU correction for isolations
                                 effAreasConfigFile = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Run3_Winter22/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_122X.txt"),
                                 # ID decisions (common to all formats)
                                 #
                                 # all IDs listed below are available given the content of "my_id_modules" defined above.
                                 # only one is exercised for this example.
                                 #
                                 eleIdMapLoose = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-RunIIIWinter22-V1-loose"),
                                 eleIdMapMedium = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-RunIIIWinter22-V1-medium"),
                                 eleIdMapTight = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-RunIIIWinter22-V1-tight"),
				 eleMVA90noIso =  cms.InputTag('egmGsfElectronIDs:mvaEleID-RunIIIWinter22-noIso-V1-wp90'),
				 eleMVA80noIso =  cms.InputTag('egmGsfElectronIDs:mvaEleID-RunIIIWinter22-noIso-V1-wp80'),
				 eleMVA90Iso    =  cms.InputTag('egmGsfElectronIDs:mvaEleID-RunIIIWinter22-iso-V1-wp90'),
				 eleMVA80Iso    =  cms.InputTag('egmGsfElectronIDs:mvaEleID-RunIIIWinter22-iso-V1-wp80'),
                                 eleIdMapTight22 = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-RunIIIWinter22-V1-tight"),
                                 eleIdMapMVA9022Iso = cms.InputTag("egmGsfElectronIDs:mvaEleID-RunIIIWinter22-iso-V1-wp90"),
				 eleMVAValuesMapTokenIso = cms.InputTag('electronMVAValueMapProducer:ElectronMVAEstimatorRun2RunIIIWinter22IsoV1Values'),		
				 eleMVAValuesMapTokenNoIso = cms.InputTag('electronMVAValueMapProducer:ElectronMVAEstimatorRun2RunIIIWinter22NoIsoV1Values'),	
                                 muInputTag = cms.InputTag("gmtStage2Digis","Muon","RECO"),
                                 egInputTag = cms.InputTag("caloStage2Digis","EGamma","RECO"),
                                 isMC = cms.bool(True),
                                 doMuon = cms.bool(True),
                                 doEle = cms.bool(False)
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( outputFile )
                                   )

process.p = cms.Path(process.egmGsfElectronIDSequence * process.ntupler)
