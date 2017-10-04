import ninjaopenfoam as ninja

import os

class SchaerWavesCP:
    def __init__(self, meshes, parallel, fast):
        fvSchemes = os.path.join('src/schaerWavesCP/fvSchemes')
        cp = ninja.SchaerWaves.charneyPhillips

        self.btf300dz = ninja.SchaerWaves('schaerWavesCP-btf-300dz', meshes.btf300dz, 8.0, cp, fvSchemes, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btf300dz)
