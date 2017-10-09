import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, meshes, parallel, fast):
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        cubicFit = os.path.join('src/schaerWaves/cubicFit')
        lorenz = ninja.SchaerWaves.lorenz

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshes.btf300dz, 8.0, lorenz, linearUpwind, parallel, fast, meshes.btfFast)
        self.cutCellLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-cutCell-300dz-linearUpwind', meshes.cutCell300dz, 8.0, lorenz, linearUpwind, parallel, fast, meshes.btfFast)
        self.slantedCellLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-slantedCell-300dz-linearUpwind', meshes.slantedCell300dz, 8.0, lorenz, linearUpwind, parallel, fast, meshes.btfFast)

        self.btfCubicFit300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-cubicFit', meshes.btf300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-cutCell-300dz-cubicFit', meshes.cutCell300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-slantedCell-300dz-cubicFit', meshes.slantedCell300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btfLinearUpwind300dz)
        build.add(self.cutCellLinearUpwind300dz)
        build.add(self.slantedCellLinearUpwind300dz)
        build.add(self.btfCubicFit300dz)
        build.add(self.cutCellCubicFit300dz)
        build.add(self.slantedCellCubicFit300dz)
