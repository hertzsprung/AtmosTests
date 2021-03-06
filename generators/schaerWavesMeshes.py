from ninjaopenfoam import BlockMesh, CutCellMesh, SlantedCellMesh, TerrainFollowingMesh

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

        createPatchDict = os.path.join('src/schaerWaves/createPatchDict')
        self.cutCell500dz = CutCellMesh('schaerWaves-mesh-cutCell-500dz', os.path.join('src/schaerWaves/mesh-cutCell-500dz'), createPatchDict)
        self.cutCell300dz = CutCellMesh('schaerWaves-mesh-cutCell-300dz', os.path.join('src/schaerWaves/mesh-cutCell-300dz'), createPatchDict)
        self.cutCell250dz = CutCellMesh('schaerWaves-mesh-cutCell-250dz', os.path.join('src/schaerWaves/mesh-cutCell-250dz'), createPatchDict)
        self.cutCell200dz = CutCellMesh('schaerWaves-mesh-cutCell-200dz', os.path.join('src/schaerWaves/mesh-cutCell-200dz'), createPatchDict)
        self.cutCell150dz = CutCellMesh('schaerWaves-mesh-cutCell-150dz', os.path.join('src/schaerWaves/mesh-cutCell-150dz'), createPatchDict)
        self.cutCell125dz = CutCellMesh('schaerWaves-mesh-cutCell-125dz', os.path.join('src/schaerWaves/mesh-cutCell-125dz'), createPatchDict)
        self.cutCell100dz = CutCellMesh('schaerWaves-mesh-cutCell-100dz', os.path.join('src/schaerWaves/mesh-cutCell-100dz'), createPatchDict)
        self.cutCell75dz = CutCellMesh('schaerWaves-mesh-cutCell-75dz', os.path.join('src/schaerWaves/mesh-cutCell-75dz'), createPatchDict)
        self.cutCell50dz = CutCellMesh('schaerWaves-mesh-cutCell-50dz', os.path.join('src/schaerWaves/mesh-cutCell-50dz'), createPatchDict)

        self.slantedCell500dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-500dz', noOrography500dz, os.path.join('src/schaerWaves/mesh-slantedCell-500dz'))
        self.slantedCell300dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-300dz', noOrography300dz, os.path.join('src/schaerWaves/mesh-slantedCell-300dz'))
        self.slantedCell250dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-250dz', noOrography250dz, os.path.join('src/schaerWaves/mesh-slantedCell-250dz'))
        self.slantedCell200dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-200dz', noOrography200dz, os.path.join('src/schaerWaves/mesh-slantedCell-200dz'))
        self.slantedCell150dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-150dz', noOrography150dz, os.path.join('src/schaerWaves/mesh-slantedCell-150dz'))
        self.slantedCell125dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-125dz', noOrography125dz, os.path.join('src/schaerWaves/mesh-slantedCell-125dz'))
        self.slantedCell100dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-100dz', noOrography100dz, os.path.join('src/schaerWaves/mesh-slantedCell-100dz'))
        self.slantedCell75dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-75dz', noOrography75dz, os.path.join('src/schaerWaves/mesh-slantedCell-75dz'))
        self.slantedCell50dz = SlantedCellMesh('schaerWaves-mesh-slantedCell-50dz', noOrography50dz, os.path.join('src/schaerWaves/mesh-slantedCell-50dz'))

        self.meshes = [
                noOrographyFast, noOrography500dz, noOrography300dz, noOrography250dz, noOrography200dz,
                noOrography150dz, noOrography125dz, noOrography100dz, noOrography75dz, noOrography50dz,
                self.btfFast, self.btf500dz, self.btf300dz, self.btf250dz, self.btf200dz, self.btf150dz, 
                self.btf125dz, self.btf100dz, self.btf75dz, self.btf50dz,
                self.cutCell500dz, self.cutCell300dz, self.cutCell250dz, self.cutCell200dz, self.cutCell150dz,
                self.cutCell125dz, self.cutCell100dz, self.cutCell75dz, self.cutCell50dz,
                self.slantedCell500dz, self.slantedCell300dz, self.slantedCell250dz, self.slantedCell200dz,
                self.slantedCell150dz, self.slantedCell125dz, self.slantedCell100dz, self.slantedCell75dz,
                self.slantedCell50dz
        ]

    def addTo(self, build):
        build.addAll(self.meshes)
