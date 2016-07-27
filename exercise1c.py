from DataFormats.FWLite import Handle, Events
import ROOT
events = Events("tracks_and_vertices_beginofrun274422.root")
tracks = Handle("std::vector<reco::Track>")

histogram = ROOT.TH1F("histogram", "histogram", 100, 0, 10)

i = 0
for event in events:
    event.getByLabel("generalTracks", tracks)
    for track in tracks.product():
	histogram.Fill(track.normalizedChi2())
    i += 1
    if i > 1000: break

c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
histogram.Draw()

