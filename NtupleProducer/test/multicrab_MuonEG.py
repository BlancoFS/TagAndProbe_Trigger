#name = 'TrigEff_HWW_EGamma_2018'

dataset = {
   'Run2018A' : '/MuonEG/Run2018A-17Sep2018-v1/MINIAOD',
   'Run2018B' : '/MuonEG/Run2018B-17Sep2018-v1/MINIAOD', 
   'Run2018C' : '/MuonEG/Run2018C-17Sep2018-v1/MINIAOD', 
   'Run2018D' : '/MuonEG/Run2018D-PromptReco-v2/MINIAOD', 
   }


#nevents = -1 
lumisPerJob = {
   'Run2018A':        100,
   'Run2018B':        100,
   'Run2018C':        100,
   'Run2018D':        100,
   }

listOfSamples = [
   'Run2018A',        
   'Run2018B',        
   'Run2018C',        
   'Run2018D',        
   ]

if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   config.General.workArea = 'crab_TrigEff_HWW_MuEG_2018'
   config.General.transferLogs = False

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler.py'
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   config.Data.splitting = 'LumiBased'
   config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/arun/TriggerEff_RunIILegacy/TrigEff_MuEG_2018'

   config.Site.storageSite ='T2_CH_CERN'
 #  config.Site.blacklist = ['T2_BR_SPRACE', 'T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = lumisPerJob[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()