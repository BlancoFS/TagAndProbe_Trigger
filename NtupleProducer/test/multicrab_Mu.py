#name = 'TrigEff_HWW_EGamma_2018'

dataset = {
   'Run2022B' : '/SingleMuon/Run2022B-22Sep2023-v1/MINIAOD',
   'Run2022C1': '/SingleMuon/Run2022C-22Sep2023-v1/MINIAOD',
   'Run2022C2': '/Muon/Run2022C-22Sep2023-v1/MINIAOD',
   'Run2022D' : '/Muon/Run2022D-22Sep2023-v1/MINIAOD',
   'Run2022E' : '/Muon/Run2022E-22Sep2023-v1/MINIAOD',
   'Run2022F' : '/Muon/Run2022F-22Sep2023-v2/MINIAOD',
   'Run2022G' : '/Muon/Run2022G-22Sep2023-v1/MINIAOD',
   "Run2023C_0v1": "/Muon0/Run2023C-22Sep2023_v1-v1/MINIAOD",
   "Run2023C_0v2": "/Muon0/Run2023C-22Sep2023_v2-v1/MINIAOD",
   "Run2023C_0v3": "/Muon0/Run2023C-22Sep2023_v3-v1/MINIAOD",
   "Run2023C_0v4": "/Muon0/Run2023C-22Sep2023_v4-v1/MINIAOD",
   "Run2023C_1v1": "/Muon1/Run2023C-22Sep2023_v1-v1/MINIAOD",
   "Run2023C_1v2": "/Muon1/Run2023C-22Sep2023_v2-v1/MINIAOD",
   "Run2023C_1v3": "/Muon1/Run2023C-22Sep2023_v3-v1/MINIAOD",
   "Run2023C_1v4": "/Muon1/Run2023C-22Sep2023_v4-v1/MINIAOD",
   "Run2023D_0v1": "/Muon0/Run2023D-22Sep2023_v1-v1/MINIAOD",
   "Run2023D_0v2": "/Muon0/Run2023D-22Sep2023_v2-v1/MINIAOD",
   "Run2023D_1v1": "/Muon1/Run2023D-22Sep2023_v1-v1/MINIAOD",
   "Run2023D_1v2": "/Muon1/Run2023D-22Sep2023_v2-v1/MINIAOD",
}
lumisPerJob = {
   'Run2022B' :        100,
   'Run2022C1':        100,
   'Run2022C2':        100,
   'Run2022D' :        100,
   'Run2022E':        100,
   'Run2022F':        100,
   'Run2022G':        100,
   "Run2023C_0v1": 100,
   "Run2023C_0v2": 100,
   "Run2023C_0v3": 100,
   "Run2023C_0v4": 100,
   "Run2023C_1v1": 100,
   "Run2023C_1v2": 100,
   "Run2023C_1v3": 100,
   "Run2023C_1v4": 100,
   "Run2023D_0v1": 100,
   "Run2023D_0v2": 100,
   "Run2023D_1v1": 100,
   "Run2023D_1v2": 100,
}
listOfSamples = [
   #'Run2022B',
   #'Run2022C1',
   #'Run2022C2',
   #'Run2022D',
   #'Run2022E',
   #'Run2022F',
   #'Run2022G',
   "Run2023C_0v1",
   "Run2023C_0v2",
   "Run2023C_0v3",
   "Run2023C_0v4",
   "Run2023C_1v1",
   "Run2023C_1v2",
   "Run2023C_1v3",
   "Run2023C_1v4",
   "Run2023D_0v1",
   "Run2023D_0v2",
   "Run2023D_1v1",
   "Run2023D_1v2",
]


if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   config.General.workArea = 'crab_TrigEff_HWW_Muon_2023'
   config.General.transferLogs = False

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler.py'
   config.JobType.allowUndistributedCMSSW = True
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   #config.Data.splitting = 'Automatic'
   config.Data.splitting = 'LumiBased'
   #config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_355100_362760_Golden.json'
   config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_366442_370790_Golden.json'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_Muon_2023'

   config.Site.storageSite ='T2_CH_CERN'
 #  config.Site.blacklist = ['T2_BR_SPRACE', 'T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
      config.Data.splitting = 'LumiBased'
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = lumisPerJob[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()
