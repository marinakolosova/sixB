from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'srosenzw_NMSSM_XYH_YToHH_6b_MX_1000_MY_700_sl7_nano_100k'
config.General.workArea        = 'srosenzw_NMSSM_XYH_YToHH_6b_MX_1000_MY_700_sl7_nano_100k'
config.General.transferOutputs = True
config.General.transferLogs    = False

config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'nanoAOD_step_fake.py'
config.JobType.maxMemoryMB = 3500
config.JobType.inputFiles  = ['scriptExe.sh', 'genSim_step.py','digiPremix_step.py','hlt_step.py','recoAOD_step.py','miniAOD_step.py','nanoAOD_step.py','NMSSM_XYH_YToHH_6b_MX_1000_MY_700_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz']
config.JobType.scriptExe   ='scriptExe.sh'
config.JobType.numCores    = 2

config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits  = 100000
# config.Data.outLFNDirBase = '/store/user/ekoenig/XYH_test_privateMC/'
config.Data.outLFNDirBase = '/store/group/lpchbb/srosenzw/XYH_YToHH/'
config.Data.publication = False
# config.Data.outputPrimaryDataset = 'ggZH_HToMuMu_ZToLL_M125_13TeV_powheg_pythia8'
config.Data.outputDatasetTag     = 'srosenzw_NMSSM_XYH_YToHH_6b_MX_1000_MY_700_sl7_nano_100k'

config.Site.storageSite = 'T3_US_FNALLPC'
