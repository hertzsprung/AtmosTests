import ninjaopenfoam as ninja

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        linearUpwind = os.path.join('src/schaerAdvect/linearUpwind')
        cubicFit = os.path.join('src/schaerAdvect/cubicFit')
        T_init = os.path.join('src/schaerWaves/theta_init')

        self.btf300dzLinearUpwind = ninja.ThermalAdvect('thermalAdvect-btf-300dz-linearUpwind', 0, meshes.btf300dz, 8, linearUpwind, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
