import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, meshes, parallel, fast):
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        cubicFit = os.path.join('src/schaerWaves/cubicFit')
        lorenz = ninja.SchaerWaves.lorenz

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshes.btf300dz, 8.0, lorenz, linearUpwind, parallel, fast, meshes.btfFast)

        self.btfCubicFit500dz = ninja.SchaerWaves('schaerWaves-btf-500dz-cubicFit', meshes.btf500dz, 13.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-cubicFit', meshes.btf300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit250dz = ninja.SchaerWaves('schaerWaves-btf-250dz-cubicFit', meshes.btf250dz, 6.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit200dz = ninja.SchaerWaves('schaerWaves-btf-200dz-cubicFit', meshes.btf200dz, 5.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit150dz = ninja.SchaerWaves('schaerWaves-btf-150dz-cubicFit', meshes.btf150dz, 4, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit125dz = ninja.SchaerWaves('schaerWaves-btf-125dz-cubicFit', meshes.btf125dz, 3.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit100dz = ninja.SchaerWaves('schaerWaves-btf-100dz-cubicFit', meshes.btf100dz, 2.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit75dz = ninja.SchaerWaves('schaerWaves-btf-75dz-cubicFit', meshes.btf75dz, 2, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.btfCubicFit50dz = ninja.SchaerWaves('schaerWaves-btf-50dz-cubicFit', meshes.btf50dz, 1.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)

        self.cutCellCubicFit500dz = ninja.SchaerWaves('schaerWaves-cutCell-500dz-cubicFit', meshes.cutCell500dz, 13.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-cutCell-300dz-cubicFit', meshes.cutCell300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit250dz = ninja.SchaerWaves('schaerWaves-cutCell-250dz-cubicFit', meshes.cutCell250dz, 6.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit200dz = ninja.SchaerWaves('schaerWaves-cutCell-200dz-cubicFit', meshes.cutCell200dz, 5.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit150dz = ninja.SchaerWaves('schaerWaves-cutCell-150dz-cubicFit', meshes.cutCell150dz, 4, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit125dz = ninja.SchaerWaves('schaerWaves-cutCell-125dz-cubicFit', meshes.cutCell125dz, 3.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit100dz = ninja.SchaerWaves('schaerWaves-cutCell-100dz-cubicFit', meshes.cutCell100dz, 2.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit75dz = ninja.SchaerWaves('schaerWaves-cutCell-75dz-cubicFit', meshes.cutCell75dz, 2, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCellCubicFit50dz = ninja.SchaerWaves('schaerWaves-cutCell-50dz-cubicFit', meshes.cutCell50dz, 1.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)

        self.slantedCellCubicFit500dz = ninja.SchaerWaves('schaerWaves-slantedCell-500dz-cubicFit', meshes.slantedCell500dz, 13.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit300dz = ninja.SchaerWaves('schaerWaves-slantedCell-300dz-cubicFit', meshes.slantedCell300dz, 8.0, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit250dz = ninja.SchaerWaves('schaerWaves-slantedCell-250dz-cubicFit', meshes.slantedCell250dz, 6.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit200dz = ninja.SchaerWaves('schaerWaves-slantedCell-200dz-cubicFit', meshes.slantedCell200dz, 5.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit150dz = ninja.SchaerWaves('schaerWaves-slantedCell-150dz-cubicFit', meshes.slantedCell150dz, 4, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit125dz = ninja.SchaerWaves('schaerWaves-slantedCell-125dz-cubicFit', meshes.slantedCell125dz, 3.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit100dz = ninja.SchaerWaves('schaerWaves-slantedCell-100dz-cubicFit', meshes.slantedCell100dz, 2.666666667, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit75dz = ninja.SchaerWaves('schaerWaves-slantedCell-75dz-cubicFit', meshes.slantedCell75dz, 2, lorenz, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCellCubicFit50dz = ninja.SchaerWaves('schaerWaves-slantedCell-50dz-cubicFit', meshes.slantedCell50dz, 1.333333333, lorenz, cubicFit, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btfLinearUpwind300dz)

        build.add(self.btfCubicFit500dz)
        build.add(self.btfCubicFit300dz)
        build.add(self.btfCubicFit250dz)
        build.add(self.btfCubicFit200dz)
        build.add(self.btfCubicFit150dz)
        build.add(self.btfCubicFit125dz)
        build.add(self.btfCubicFit100dz)
        build.add(self.btfCubicFit75dz)
        build.add(self.btfCubicFit50dz)

        build.add(self.cutCellCubicFit500dz)
        build.add(self.cutCellCubicFit300dz)
        build.add(self.cutCellCubicFit250dz)
        build.add(self.cutCellCubicFit200dz)
        build.add(self.cutCellCubicFit150dz)
        build.add(self.cutCellCubicFit125dz)
        build.add(self.cutCellCubicFit100dz)
        build.add(self.cutCellCubicFit75dz)
        build.add(self.cutCellCubicFit50dz)

        build.add(self.slantedCellCubicFit500dz)
        build.add(self.slantedCellCubicFit300dz)
        build.add(self.slantedCellCubicFit250dz)
        build.add(self.slantedCellCubicFit200dz)
        build.add(self.slantedCellCubicFit150dz)
        build.add(self.slantedCellCubicFit125dz)
        build.add(self.slantedCellCubicFit100dz)
        build.add(self.slantedCellCubicFit75dz)
        build.add(self.slantedCellCubicFit50dz)
