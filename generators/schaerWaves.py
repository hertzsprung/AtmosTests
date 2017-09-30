import ninjaopenfoam as ninja

import os

class SchaerWaves:
    def __init__(self, meshes, parallel, fast):
        linearUpwind = os.path.join('src/schaerWaves/linearUpwind')
        cubicFit = os.path.join('src/schaerWaves/cubicFit')

        self.btfLinearUpwind300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-linearUpwind', meshes.btf300dz, 8.0, linearUpwind, parallel, fast, meshes.btfFast)
        self.btfCubicFit300dz = ninja.SchaerWaves('schaerWaves-btf-300dz-cubicFit', meshes.btf300dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)

        self.btfCubicFit50dz = ninja.SchaerWaves('schaerWaves-btf-50dz-cubicFit', meshes.btf50dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btfLinearUpwind300dz)
        build.add(self.btfCubicFit300dz)
        build.add(self.btfCubicFit50dz)
