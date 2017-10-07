import ninjaopenfoam as ninja
from ninjaopenfoam import BlockMesh

import os

class ArakawaKonor:
    def __init__(self, parallel, fast):
        lorenz = ninja.ArakawaKonor.lorenz
        cp = ninja.ArakawaKonor.charneyPhillips
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        fvSchemesCP = os.path.join('src/schaerWavesCP/fvSchemes')

        self.meshFast = BlockMesh('arakawaKonor-mesh-fast', os.path.join('src/arakawaKonor/mesh-fast'))
        self.meshUniform = BlockMesh('arakawaKonor-mesh-uniform', os.path.join('src/arakawaKonor/mesh-uniform'))

        self.uniformLorenz = ninja.ArakawaKonor('arakawaKonor-uniform-lorenz', self.meshUniform, lorenz, linearUpwind, parallel, fast, self.meshFast)
        self.uniformCP = ninja.ArakawaKonor('arakawaKonor-uniform-cp', self.meshUniform, cp, fvSchemesCP, parallel, fast, self.meshFast)

    def addTo(self, build):
        build.add(self.meshUniform)
        build.add(self.meshFast)
        build.add(self.uniformLorenz)
        build.add(self.uniformCP)
