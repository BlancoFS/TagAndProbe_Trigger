#name = 'TrigEff_HWW_EGamma_2018'

dataset = {
   'Run2022B' : '/SingleMuon/Run2022B-22Sep2023-v1/MINIAOD',
   'Run2022C1' : '/SingleMuon/Run2022C-22Sep2023-v1/MINIAOD',
   'Run2022C2' : '/Muon/Run2022C-22Sep2023-v1/MINIAOD',
   'Run2022D' : '/Muon/Run2022D-22Sep2023-v1/MINIAOD',
}
lumisPerJob = {
   'Run2022B' :        100,
   'Run2022C1':        100,
   'Run2022C2':        100,
   'Run2022D' :        100,
}
listOfSamples = [
   'Run2022B',
   'Run2022C1',
   'Run2022C2',
   'Run2022D',
]

'''
dataset = {
   'Run2022E' : '/Muon/Run2022E-22Sep2023-v1/MINIAOD',
}
lumisPerJob = {
   'Run2022E':        100,
}
listOfSamples = [
   'Run2022E',
]
'''

'''
### Run2022EE Prompt
dataset = {
   'Run2022F' : '/Muon/Run2022F-PromptReco-v1/MINIAOD',
   'Run2022G' : '/Muon/Run2022G-PromptReco-v1/MINIAOD',
}

#nevents = -1 
lumisPerJob = {
   'Run2022F':        100,
   'Run2022G':        100,
   }

listOfSamples = [
   'Run2022F',        
   'Run2022G',        
   ]
'''

if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   config.General.workArea = 'crab_TrigEff_HWW_Muon_2022'
   config.General.transferLogs = False

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler.py'
   config.JobType.allowUndistributedCMSSW = True
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   #config.Data.splitting = 'Automatic'
   config.Data.splitting = 'LumiBased'
   config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_355100_362760_Golden.json'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_prompt/TrigEff_HWW_Muon_2022ReReco'

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
