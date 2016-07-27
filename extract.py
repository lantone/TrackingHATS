import FWCore.ParameterSet.Config as cms

process = cms.Process("TracksAndVertices")

# get the data from the Double-Mu triggered sample, a randomly selected file from Run2012A (must be accessible on your system)
process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring("/store/data/Run2015D/DoubleMuon/AOD/PromptReco-v4/000/260/538/00000/324F14A3-4D83-E511-B0E1-02163E012A0C.root"))
#	fileNames = cms.untracked.vstring("/store/data/Run2016B/DoubleMuon/AOD/PromptReco-v2/000/274/422/00000/02F18325-492D-E611-B768-02163E01415E.root")
	fileNames = cms.untracked.vstring("/store/data/Run2016B/DoubleMuon/AOD/PromptReco-v2/000/274/422/00000/1241192A-D72C-E611-B77F-02163E01472E.root")
)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))  # get the first 1e4 events

# ignore any messages except ERROR level and higher
process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring("cout"),
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR")))

# don't exclude any events

# output to tracks_and_vertices.root
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("drop *",   # exclude all but a few chosen data products
                                           
                                           # tracks of all kinds
                                           "keep *_generalTracks_*_*",
                                           "keep *_globalMuons_*_*",
                                           "keep *_ckfInOutTracksFromConversions_*_*",
                                           "keep *_ckfOutInTracksFromConversions_*_*",
                                           "keep *_conversionStepTracks_*_*",
                                           "keep *_uncleanedOnlyCkfInOutTracksFromConversions_*_*",
                                           "keep *_uncleanedOnlyCkfOutInTracksFromConversions_*_*",
					   "keep *_cosmicMuons_*_*",
					   "keep *_cosmicMuons1Leg_*_*",
					   "keep *_displacedGlobalMuons_*_*",
					   "keep *_displacedStandAloneMuons_*_*",
					   "keep *_displacedTracks_*_*",
					   "keep *_refittedStandAloneMuons_*_*",
					   "keep *_standAloneMuons_*_*",
					   "keep *_tevMuons_*_*",
					   "keep *_impactParameterTagInfosEI_*_*",
                                           
                                           # the beamspot and primary vertices
                                           "keep *_offlineBeamSpot_*_*",
                                           "keep *_offlinePrimaryVertices_*_*",
                                           "keep *_offlinePrimaryVerticesWithBS_*_*",
					   "keep *_inclusiveSecondaryVertices_*_*",

					   #keep a few other things
					   "keep *_generalV0Candidates_*_*",

                                           # event-level information that we *might* use
                                           "keep *_logErrorHarvester_*_*",
                                           "keep *_l1L1GtObjectMap_*_*",
                                           "keep *_TriggerResults_*_HLT",
                                           "keep *_hltTriggerSummaryAOD_*_*",
                                           "keep *_clusterSummaryProducer_*_*",
                                           ),
    fileName = cms.untracked.string("tracks_and_vertices_beginofrun274422.root"))

process.endpath = cms.EndPath(process.output)
