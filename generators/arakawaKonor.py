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
        self.meshHorizontalGrading = BlockMesh('arakawaKonor-mesh-horizontalGrading', os.path.join('src/arakawaKonor/mesh-horizontalGrading'))
        self.meshVerticalGrading = BlockMesh('arakawaKonor-mesh-verticalGrading', os.path.join('src/arakawaKonor/mesh-verticalGrading'))

        self.uniformLorenz = ninja.ArakawaKonor('arakawaKonor-uniform-lorenz', self.meshUniform, lorenz, linearUpwind, parallel, fast, self.meshFast)
        self.uniformCP = ninja.ArakawaKonor('arakawaKonor-uniform-cp', self.meshUniform, cp, fvSchemesCP, parallel, fast, self.meshFast)

        self.horizontalGradingLorenz = ninja.ArakawaKonor('arakawaKonor-horizontalGrading-lorenz', self.meshHorizontalGrading, lorenz, linearUpwind, parallel, fast, self.meshFast)
        self.horizontalGradingCP = ninja.ArakawaKonor('arakawaKonor-horizontalGrading-cp', self.meshHorizontalGrading, cp, fvSchemesCP, parallel, fast, self.meshFast)

        self.verticalGradingLorenz = ninja.ArakawaKonor('arakawaKonor-verticalGrading-lorenz', self.meshVerticalGrading, lorenz, linearUpwind, parallel, fast, self.meshFast)
        self.verticalGradingCP = ninja.ArakawaKonor('arakawaKonor-verticalGrading-cp', self.meshVerticalGrading, cp, fvSchemesCP, parallel, fast, self.meshFast)

    def addTo(self, build):
        build.add(self.meshFast)
        build.add(self.meshUniform)
        build.add(self.meshHorizontalGrading)
        build.add(self.meshVerticalGrading)
        build.add(self.uniformLorenz)
        build.add(self.uniformCP)
        build.add(self.horizontalGradingLorenz)
        build.add(self.horizontalGradingCP)
        build.add(self.verticalGradingLorenz)
        build.add(self.verticalGradingCP)
