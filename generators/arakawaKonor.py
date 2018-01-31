import ninjaopenfoam as ninja

import os

class ArakawaKonor:
    def __init__(self, meshes, parallel, fast):
        lorenz = ninja.ArakawaKonor.lorenz
        cp = ninja.ArakawaKonor.charneyPhillips
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        fvSchemesCP = os.path.join('src/schaerWavesCP/fvSchemes')

        self.uniformLorenz = ninja.ArakawaKonor('arakawaKonor-uniform-lorenz', meshes.uniform, lorenz, linearUpwind, parallel, fast, meshes.fast)
        self.uniformCP = ninja.ArakawaKonor('arakawaKonor-uniform-cp', meshes.uniform, cp, fvSchemesCP, parallel, fast, meshes.fast)

        self.horizontalGradingLorenz = ninja.ArakawaKonor('arakawaKonor-horizontalGrading-lorenz', meshes.horizontalGrading, lorenz, linearUpwind, parallel, fast, meshes.fast)
        self.horizontalGradingCP = ninja.ArakawaKonor('arakawaKonor-horizontalGrading-cp', meshes.horizontalGrading, cp, fvSchemesCP, parallel, fast, meshes.fast)

        self.verticalGradingLorenz = ninja.ArakawaKonor('arakawaKonor-verticalGrading-lorenz', meshes.verticalGrading, lorenz, linearUpwind, parallel, fast, meshes.fast)
        self.verticalGradingCP = ninja.ArakawaKonor('arakawaKonor-verticalGrading-cp', meshes.verticalGrading, cp, fvSchemesCP, parallel, fast, meshes.fast, endTime=10950)

    def addTo(self, build):
        build.add(self.uniformLorenz)
        build.add(self.uniformCP)
        build.add(self.horizontalGradingLorenz)
        build.add(self.horizontalGradingCP)
        build.add(self.verticalGradingLorenz)
        build.add(self.verticalGradingCP)
