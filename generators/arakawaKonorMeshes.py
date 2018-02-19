from ninjaopenfoam import BlockMesh

import os

class ArakawaKonorMeshes:
    def __init__(self):
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')

        self.fast = BlockMesh('arakawaKonor-mesh-fast', os.path.join('src/arakawaKonor/mesh-fast'))
        self.uniform = BlockMesh('arakawaKonor-mesh-uniform', os.path.join('src/arakawaKonor/mesh-uniform'))
        self.uniformFine = BlockMesh('arakawaKonor-mesh-uniformFine', os.path.join('src/arakawaKonor/mesh-uniformFine'))
        self.horizontalGrading = BlockMesh('arakawaKonor-mesh-horizontalGrading', os.path.join('src/arakawaKonor/mesh-horizontalGrading'))
        self.verticalGrading = BlockMesh('arakawaKonor-mesh-verticalGrading', os.path.join('src/arakawaKonor/mesh-verticalGrading'))

    def addTo(self, build):
        build.add(self.fast)
        build.add(self.uniform)
        build.add(self.uniformFine)
        build.add(self.horizontalGrading)
        build.add(self.verticalGrading)
