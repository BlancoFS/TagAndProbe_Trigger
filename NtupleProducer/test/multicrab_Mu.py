#name = 'TrigEff_HWW_EGamma_2018'

dataset = {
   'Run2018A' : '/SingleMuon/Run2018A-12Nov2019_UL2018_rsb-v1/MINIAOD',
   'Run2018B' : '/SingleMuon/Run2018B-12Nov2019_UL2018-v2/MINIAOD', 
   'Run2018C' : '/SingleMuon/Run2018C-12Nov2019_UL2018-v2/MINIAOD', 
   'Run2018D' : '/SingleMuon/Run2018D-12Nov2019_UL2018-v4/MINIAOD', 
   }


#nevents = -1 
lumisPerJob = {
   'Run2018A':        200,
   'Run2018B':        200,
   'Run2018C':        200,
   'Run2018D':        200,
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

   config.General.workArea = 'crab_TrigEff_HWW_Muon_2018'
   config.General.transferLogs = False

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler.py'
   config.JobType.allowUndistributedCMSSW = True
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   config.Data.splitting = 'Automatic'
   #config.Data.splitting = 'LumiBased'
   config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/arun/TriggerEff_RunII_ULLegacy/TrigEff_HWW_Muon_2018'

   config.Site.storageSite ='T2_CH_CERN'
 #  config.Site.blacklist = ['T2_BR_SPRACE', 'T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
#      config.Data.splitting = 'Automatic'
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = lumisPerJob[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()