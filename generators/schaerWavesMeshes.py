from ninjaopenfoam import BlockMesh, TerrainFollowingMesh

import os

class SchaerWavesMeshes:
    def __init__(self):
        noOrographyFast = BlockMesh('schaerWaves-mesh-noOrography-fast', os.path.join('src/schaerWaves/mesh-noOrography-fast'))
        noOrography500dz = BlockMesh('schaerWaves-mesh-noOrography-500dz', os.path.join('src/schaerWaves/mesh-noOrography-500dz'))
        noOrography300dz = BlockMesh('schaerWaves-mesh-noOrography-300dz', os.path.join('src/schaerWaves/mesh-noOrography-300dz'))
        noOrography250dz = BlockMesh('schaerWaves-mesh-noOrography-250dz', os.path.join('src/schaerWaves/mesh-noOrography-250dz'))
        noOrography200dz = BlockMesh('schaerWaves-mesh-noOrography-200dz', os.path.join('src/schaerWaves/mesh-noOrography-200dz'))
        noOrography150dz = BlockMesh('schaerWaves-mesh-noOrography-150dz', os.path.join('src/schaerWaves/mesh-noOrography-150dz'))
        noOrography125dz = BlockMesh('schaerWaves-mesh-noOrography-125dz', os.path.join('src/schaerWaves/mesh-noOrography-125dz'))
        noOrography100dz = BlockMesh('schaerWaves-mesh-noOrography-100dz', os.path.join('src/schaerWaves/mesh-noOrography-100dz'))
        noOrography75dz = BlockMesh('schaerWaves-mesh-noOrography-75dz', os.path.join('src/schaerWaves/mesh-noOrography-75dz'))
        noOrography50dz = BlockMesh('schaerWaves-mesh-noOrography-50dz', os.path.join('src/schaerWaves/mesh-noOrography-50dz'))

        btfDict = os.path.join('src/schaerWaves/mesh-btf')
        self.btfFast = TerrainFollowingMesh('schaerWaves-mesh-btf-fast', noOrographyFast, btfDict)
        self.btf500dz = TerrainFollowingMesh('schaerWaves-mesh-btf-500dz', noOrography500dz, btfDict)
        self.btf300dz = TerrainFollowingMesh('schaerWaves-mesh-btf-300dz', noOrography300dz, btfDict)
        self.btf250dz = TerrainFollowingMesh('schaerWaves-mesh-btf-250dz', noOrography250dz, btfDict)
        self.btf200dz = TerrainFollowingMesh('schaerWaves-mesh-btf-200dz', noOrography200dz, btfDict)
        self.btf150dz = TerrainFollowingMesh('schaerWaves-mesh-btf-150dz', noOrography150dz, btfDict)
        self.btf125dz = TerrainFollowingMesh('schaerWaves-mesh-btf-125dz', noOrography125dz, btfDict)
        self.btf100dz = TerrainFollowingMesh('schaerWaves-mesh-btf-100dz', noOrography100dz, btfDict)
        self.btf75dz = TerrainFollowingMesh('schaerWaves-mesh-btf-75dz', noOrography75dz, btfDict)
        self.btf50dz = TerrainFollowingMesh('schaerWaves-mesh-btf-50dz', noOrography50dz, btfDict)

        self.meshes = [
                noOrographyFast, noOrography500dz, noOrography300dz, noOrography250dz, noOrography200dz,
                noOrography150dz, noOrography125dz, noOrography100dz, noOrography75dz, noOrography50dz,
                self.btfFast, self.btf500dz, self.btf300dz, self.btf250dz, self.btf200dz, self.btf150dz, 
                self.btf125dz, self.btf100dz, self.btf75dz, self.btf50dz
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
