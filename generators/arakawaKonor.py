import ninjaopenfoam as ninja
from ninjaopenfoam import BlockMesh

import os

class ArakawaKonor:
    def __init__(self, parallel, fast):
        lorenz = ninja.ArakawaKonor.lorenz
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')

        self.meshUniform = BlockMesh('arakawaKonor-mesh-uniform', os.path.join('src/arakawaKonor/mesh-uniform'))
        self.uniform = ninja.ArakawaKonor('arakawaKonor-uniform', self.meshUniform, lorenz, linearUpwind, parallel, fast)

    def addTo(self, build):
        build.add(self.meshUniform)
        build.add(self.uniform)
