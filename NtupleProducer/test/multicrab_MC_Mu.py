#name = 'TrigEff_HWW_EGamma_2018'

dataset = {
   'DYto2Mu_24' : '/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v1-v4/MINIAODSIM',
}

nevents = -1 

listOfSamples = [
   'DYto2Mu_24'
]

if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   config.General.workArea = 'crab_TrigEff_HWW_DYto2Mu_2024'
   config.General.transferLogs = False

   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler_MC_Mu.py'
   config.JobType.allowUndistributedCMSSW = True
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   config.Data.splitting = 'FileBased'
   #config.Data.splitting = 'LumiBased'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/TriggerEff_RunIII_Summer24/TrigEff_HWW_DYto2Mu_2024'

   config.Site.storageSite = 'T2_CH_CERN'

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
      config.Data.splitting = 'FileBased'
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = 1
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()
