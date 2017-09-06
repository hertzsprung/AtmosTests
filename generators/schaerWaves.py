from ninjaopenfoam import BlockMesh, TerrainFollowingMesh

import os

class SchaerWaves:
    def __init__(self, parallel, fast):
        meshNoOrography300dz = BlockMesh('schaerWaves-mesh-noOrography-300dz', os.path.join('src/schaerWaves/mesh-noOrography-300dz'))

        meshBtf300dz = TerrainFollowingMesh('schaerWaves-mesh-btf-300dz', meshNoOrography300dz, os.path.join('src/schaerWaves/mesh-btf'))

        self.meshes = [
                meshNoOrography300dz,
                meshBtf300dz
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
