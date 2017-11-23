import ninjaopenfoam as ninja

import os

class ArakawaKonorAdvect:
    def __init__(self, meshes, parallel, fast):
        lorenz = ninja.ArakawaKonor.lorenz
        cp = ninja.ArakawaKonor.charneyPhillips
        linearUpwind = os.path.join('src/schaerAdvect/linearUpwind')

        self.uniformLorenz = ninja.ArakawaKonorAdvect('arakawaKonorAdvect-uniform-lorenz', meshes.uniform, lorenz, linearUpwind, parallel, fast, meshes.fast)

    def addTo(self, build):
        build.add(self.uniformLorenz)
