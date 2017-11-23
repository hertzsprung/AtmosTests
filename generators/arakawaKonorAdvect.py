import ninjaopenfoam as ninja

import os

class ArakawaKonorAdvect:
    def __init__(self, meshes, parallel, fast):
        lorenz = ninja.ArakawaKonor.lorenz
        cp = ninja.ArakawaKonor.charneyPhillips
        linearUpwind = os.path.join('src/schaerAdvect/linearUpwind')
        cpFvSchemes = os.path.join('src/arakawaKonorAdvect/charneyPhillipsFvSchemes')

        self.uniformLorenz = ninja.ArakawaKonorAdvect('arakawaKonorAdvect-uniform-lorenz', meshes.uniform, lorenz, linearUpwind, parallel, fast, meshes.fast)
        self.uniformCP = ninja.ArakawaKonorAdvect('arakawaKonorAdvect-uniform-cp', meshes.uniform, cp, cpFvSchemes, parallel, fast, meshes.fast)

    def addTo(self, build):
        build.add(self.uniformLorenz)
        build.add(self.uniformCP)
