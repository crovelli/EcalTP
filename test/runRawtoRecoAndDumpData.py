# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 92X_upgrade2017_realistic_v10 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2017 --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

#from Configuration.StandardSequences.Eras import eras
#process = cms.Process('RECO',eras.Run2_2017)

process = cms.Process('myreco')


from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.parseArguments()




# import of standard configurations
#process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
#process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
#process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
#process.load('CommonTools.ParticleFlow.EITopPAG_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')



process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(5)
    input = cms.untracked.int32(options.maxEvents)
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
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v8', '')

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




#process.simEcalTriggerPrimitiveDigis = cms.EDProducer("EcalTrigPrimProducer",
    #BarrelOnly = cms.bool(False),
    #Debug = cms.bool(False),
    #Famos = cms.bool(False),
    #InstanceEB = cms.string(''),
    #InstanceEE = cms.string(''),
    #Label = cms.string('simEcalUnsuppressedDigis'),
    #TcpOutput = cms.bool(False),
    #binOfMaximum = cms.int32(6)
#)




process.ecalTriggerPrimitiveDigis = cms.EDProducer("EcalTrigPrimProducer",
    InstanceEB = cms.string('ebDigis'),
    InstanceEE = cms.string('eeDigis'),
    Label = cms.string('ecalDigis'),

    BarrelOnly = cms.bool(False),
    Famos = cms.bool(False),
    TcpOutput = cms.bool(False),

    Debug = cms.bool(False),

    binOfMaximum = cms.int32(6), ## optional from release 200 on, from 1-10
                                                   
#    TTFHighEnergyEB = cms.double(1.0),
#    TTFHighEnergyEE = cms.double(1.0),
#    TTFLowEnergyEB = cms.double(1.0), ## this + the following is added from 140_pre4 on
#    TTFLowEnergyEE = cms.double(1.0)
)

process.ecalTriggerPrimitiveDigis_step = cms.Path(process.ecalTriggerPrimitiveDigis)


process.TFileService = cms.Service("TFileService",
     fileName = cms.string(options.outputFile)
)



#
# weights rechits 
#
process.load('RecoLocalCalo.EcalRecProducers.ecalUncalibRecHit_cfi')
process.ecalUncalibRecHit.EBdigiCollection = cms.InputTag("ecalDigis","ebDigis")
process.ecalUncalibRecHit.EEdigiCollection = cms.InputTag("ecalDigis","eeDigis")
process.weights = cms.Path(process.ecalUncalibRecHit)



#
# change the default into weights
#
process.ecalRecHit.EEuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEE")
process.ecalRecHit.EBuncalibRecHitCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEB")
#
#
#





process.TreeProducer = cms.EDAnalyzer('TreeProducer',

                           EBDigiCollection = cms.InputTag("ecalDigis","ebDigis"),
                           EEDigiCollection = cms.InputTag("ecalDigis","eeDigis"),
                           #EBDigiCollection = cms.InputTag("selectDigi","selectedEcalEBDigiCollection"),
                           #EEDigiCollection = cms.InputTag("selectDigi","selectedEcalEEDigiCollection"),

                           #EcalUncalibRecHitsEBCollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB"),
                           #EcalUncalibRecHitsEECollection = cms.InputTag("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEE"),
                           
                           #EcalUncalibRecHitsEBCollection = cms.InputTag("ecalRecHit",  "EcalRecHitsEB"),
                           #EcalUncalibRecHitsEECollection = cms.InputTag("ecalRecHit",  "EcalRecHitsEE"),

                           EcalUncalibRecHitsEBCollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEB"),
                           EcalUncalibRecHitsEECollection = cms.InputTag("ecalUncalibRecHit","EcalUncalibRecHitsEE"),


                           EBRecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
                           EERecHitCollectionLabel = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
                   
                           TPCollection = cms.InputTag("ecalDigis","EcalTriggerPrimitives"),

                           TPEmuCollection = cms.InputTag("ecalTriggerPrimitiveDigis"),
                           
                           )




process.ecalDigis_step = cms.Path(process.ecalDigis)
#process.multifit = cms.Path(process.ecalMultiFitUncalibRecHit)

process.TreeProducer_step = cms.Path(process.TreeProducer)





##################################
#### costumization for Stage2 ####

from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
#process = customizeHLTforAll(process,"GRun",_customInfo)

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
process = customizeHLTforCMSSW(process,"GRun")




process.options.allowUnscheduled = cms.untracked.bool(True)


# Schedule definition
process.schedule = cms.Schedule(
          process.raw2digi_step,
          process.reconstruction_step,
          process.ecalDigis_step,
          #process.multifit
          process.ecalTriggerPrimitiveDigis_step,
          process.weights,
          process.TreeProducer_step
          )
  
  
  
# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.pEcalAlignment,process.RECOSIMoutput_step)
#process.schedule = cms.Schedule(process.pEcalAlignment)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)


# Customisation from command line
from Configuration.DataProcessing.RecoTLR import customiseDataRun2Common 

#call to customisation function customiseDataRun2Common imported from Configuration.DataProcessing.RecoTLR
process = customiseDataRun2Common(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion


