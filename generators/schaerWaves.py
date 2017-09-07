from ninjaopenfoam import BlockMesh, TerrainFollowingMesh

import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, parallel, fast):
        meshNoOrographyFast = BlockMesh('schaerWaves-mesh-noOrography-fast', os.path.join('src/schaerWaves/mesh-noOrography-fast'))
        meshNoOrography300dz = BlockMesh('schaerWaves-mesh-noOrography-300dz', os.path.join('src/schaerWaves/mesh-noOrography-300dz'))

        meshBtfDict = os.path.join('src/schaerWaves/mesh-btf')
        meshBtfFast = TerrainFollowingMesh('schaerWaves-mesh-btf-fast', meshNoOrographyFast, meshBtfDict)
        meshBtf300dz = TerrainFollowingMesh('schaerWaves-mesh-btf-300dz', meshNoOrography300dz, meshBtfDict)

        self.meshes = [
                meshNoOrographyFast, meshNoOrography300dz,
                meshBtfFast, meshBtf300dz
        ]

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshBtf300dz, 8.0, os.path.join('src/schaerWaves/linearUpwind'), parallel, fast, meshBtfFast)

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind300dz)
