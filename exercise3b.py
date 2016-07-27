from ROOT import *
from math import sqrt
from DataFormats.FWLite import Handle, Events
events = Events("output.root")
secondaryVertices = Handle("std::vector<reco::VertexCompositeCandidate>")
mass_histogram = TH1F("mass", "mass", 100, 0.4, 0.6)
dxy_histogram = TH1F("dxy","dxy",100,0,50)

i = 0
events.toBegin()
for event in events:
    print "Event:", i
    event.getByLabel("SecondaryVerticesFromLooseTracks", "Kshort", secondaryVertices)
    j = 0
    for vertex in secondaryVertices.product():
        print "    Vertex:", j, vertex.vx(), vertex.vy(), vertex.vz()
        j += 1
        mass_histogram.Fill(vertex.mass())
        dxy_histogram.Fill(sqrt(vertex.vx()**2 + vertex.vy()**2))
    i += 1
c = TCanvas ( "c" , "c" , 800, 800 )
mass_histogram.Draw()
c.SaveAs("sec_vert_mass.png")
dxy_histogram.Draw()
c.SaveAs("sec_vert_dxy.png")
