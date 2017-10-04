import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, meshes, parallel, fast):
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        cubicFit = os.path.join('src/schaerWaves/cubicFit')

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshes.btf300dz, 8.0, linearUpwind, parallel, fast, meshes.btfFast)

        self.btfCubicFit500dz = ninja.SchaerWaves('schaerWaves-btf-500dz-cubicFit', meshes.btf500dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-cubicFit', meshes.btf300dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit50dz = ninja.SchaerWaves('schaerWaves-btf-50dz-cubicFit', meshes.btf50dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)

        self.cutCellCubicFit500dz = ninja.SchaerWaves('schaerWaves-cutCell-500dz-cubicFit', meshes.cutCell500dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-cutCell-300dz-cubicFit', meshes.cutCell300dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)

        self.slantedCellCubicFit500dz = ninja.SchaerWaves('schaerWaves-slantedCell-500dz-cubicFit', meshes.slantedCell500dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-slantedCell-300dz-cubicFit', meshes.slantedCell300dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btfLinearUpwind300dz)

        build.add(self.btfCubicFit500dz)
        build.add(self.btfCubicFit300dz)
        build.add(self.btfCubicFit50dz)

        build.add(self.cutCellCubicFit500dz)
        build.add(self.cutCellCubicFit300dz)

        build.add(self.slantedCellCubicFit500dz)
        build.add(self.slantedCellCubicFit300dz)
