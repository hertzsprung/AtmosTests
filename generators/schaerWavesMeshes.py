from ninjaopenfoam import BlockMesh, TerrainFollowingMesh

import os

class SchaerWavesMeshes:
    def __init__(self):
        # 500, 300, 250, 200, 150, 125, 100, 75, 50

        noOrographyFast = BlockMesh('schaerWaves-mesh-noOrography-fast', os.path.join('src/schaerWaves/mesh-noOrography-fast'))
        noOrography300dz = BlockMesh('schaerWaves-mesh-noOrography-300dz', os.path.join('src/schaerWaves/mesh-noOrography-300dz'))
        noOrography150dz = BlockMesh('schaerWaves-mesh-noOrography-150dz', os.path.join('src/schaerWaves/mesh-noOrography-150dz'))
        noOrography50dz = BlockMesh('schaerWaves-mesh-noOrography-50dz', os.path.join('src/schaerWaves/mesh-noOrography-50dz'))

        btfDict = os.path.join('src/schaerWaves/mesh-btf')
        self.btfFast = TerrainFollowingMesh('schaerWaves-mesh-btf-fast', noOrographyFast, btfDict)
        self.btf300dz = TerrainFollowingMesh('schaerWaves-mesh-btf-300dz', noOrography300dz, btfDict)
        self.btf150dz = TerrainFollowingMesh('schaerWaves-mesh-btf-150dz', noOrography150dz, btfDict)
        self.btf50dz = TerrainFollowingMesh('schaerWaves-mesh-btf-50dz', noOrography50dz, btfDict)

        self.meshes = [
                noOrographyFast, noOrography300dz, noOrography150dz, noOrography50dz,
                self.btfFast, self.btf300dz, self.btf150dz, self.btf50dz
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
