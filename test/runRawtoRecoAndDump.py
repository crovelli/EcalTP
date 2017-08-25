# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 92X_upgrade2017_realistic_v10 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2017 --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017)



from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.parseArguments()




# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v10', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
#process.eventinterpretaion_step = cms.Path(process.EIsequence)
#process.endjob_step = cms.EndPath(process.endOfProcess)
#process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)






# 
# re-run local reconstruction
#


#process.load('RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi')
#process.ecalMultiFitUncalibRecHit.EBdigiCollection = cms.InputTag("selectDigi","selectedEcalEBDigiCollection")
#process.ecalMultiFitUncalibRecHit.EEdigiCollection = cms.InputTag("selectDigi","selectedEcalEEDigiCollection")
#process.ecalMultiFitUncalibRecHit.EBdigiCollection = cms.InputTag("ecalDigis","ebDigis")
#process.ecalMultiFitUncalibRecHit.EEdigiCollection = cms.InputTag("ecalDigis","eeDigis")
#process.ecalMultiFitUncalibRecHit.algoPSet.useLumiInfoRunHeader = cms.bool(False)



process.TFileService = cms.Service("TFileService",
     fileName = cms.string(options.outputFile)
)


process.TreeProducer = cms.EDAnalyzer('TreeProducer',

                           EBDigiCollection = cms.InputTag("ecalDigis","ebDigis"),
                           EEDigiCollection = cms.InputTag("ecalDigis","eeDigis"),
                           #EBDigiCollection = cms.InputTag("selectDigi","selectedEcalEBDigiCollection"),
                           #EEDigiCollection = cms.InputTag("selectDigi","selectedEcalEEDigiCollection"),

                           EcalUncalibRecHitsEBCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
                           EcalUncalibRecHitsEECollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
                           #EcalUncalibRecHitsEBCollection = cms.InputTag("ecalRecHit",  "EcalRecHitsEB"),
                           #EcalUncalibRecHitsEECollection = cms.InputTag("ecalRecHit",  "EcalRecHitsEE"),

                           )




process.ecalDigis_step = cms.Path(process.ecalDigis)
#process.multifit = cms.Path(process.ecalMultiFitUncalibRecHit)

process.TreeProducer_step = cms.Path(process.TreeProducer)










# Schedule definition
process.schedule = cms.Schedule(
          process.raw2digi_step,
          process.reconstruction_step,
          process.ecalDigis_step,
          #process.multifit
          process.TreeProducer_step
          )
                                
                                
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion