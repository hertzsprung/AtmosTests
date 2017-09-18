from ninjaopenfoam import BlockMesh, TerrainFollowingMesh

import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, parallel, fast):
        meshNoOrographyFast = BlockMesh('schaerWaves-mesh-noOrography-fast', os.path.join('src/schaerWaves/mesh-noOrography-fast'))
        meshNoOrography300dz = BlockMesh('schaerWaves-mesh-noOrography-300dz', os.path.join('src/schaerWaves/mesh-noOrography-300dz'))
        meshNoOrography50dz = BlockMesh('schaerWaves-mesh-noOrography-50dz', os.path.join('src/schaerWaves/mesh-noOrography-50dz'))

        meshBtfDict = os.path.join('src/schaerWaves/mesh-btf')
        meshBtfFast = TerrainFollowingMesh('schaerWaves-mesh-btf-fast', meshNoOrographyFast, meshBtfDict)
        meshBtf300dz = TerrainFollowingMesh('schaerWaves-mesh-btf-300dz', meshNoOrography300dz, meshBtfDict)
        meshBtf50dz = TerrainFollowingMesh('schaerWaves-mesh-btf-50dz', meshNoOrography50dz, meshBtfDict)

        self.meshes = [
                meshNoOrographyFast, meshNoOrography300dz, meshNoOrography50dz,
                meshBtfFast, meshBtf300dz, meshBtf50dz
        ]

        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        cubicFit = os.path.join('src/schaerWaves/cubicFit')

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshBtf300dz, 8.0, linearUpwind, parallel, fast, meshBtfFast)
        self.btfCubicFit300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-cubicFit', meshBtf300dz, 8.0, cubicFit, parallel, fast, meshBtfFast)

        self.btfCubicFit50dz = ninja.SchaerWaves('schaerWaves-btf-50dz-cubicFit', meshBtf50dz, 8.0, cubicFit, parallel, fast, meshBtfFast)

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind300dz)
        build.add(self.btfCubicFit300dz)
        build.add(self.btfCubicFit50dz)
