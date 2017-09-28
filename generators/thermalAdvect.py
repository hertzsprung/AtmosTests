from ninjaopenfoam import Advect, Timing

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        linearUpwind = os.path.join('src/schaerAdvect/linearUpwind')
        cubicFit = os.path.join('src/schaerAdvect/cubicFit')
        T_init = os.path.join('src/schaerWaves/theta_init')

        self.btf300dzLinearUpwind = Advect('thermalAdvect-btf-300dz-linearUpwind', 0, 250, meshes.btf300dz, tracerField, velocityField, T_init, Timing(18000, 3600, 8), linearUpwind, parallel, fast)
        self.btf300dzCubicFit = Advect('thermalAdvect-btf-300dz-cubicFit', 0, 250, meshes.btf300dz, tracerField, velocityField, T_init, Timing(18000, 3600, 8), cubicFit, parallel, fast)

        self.btf150dzLinearUpwind = Advect('thermalAdvect-btf-150dz-linearUpwind', 0, 125, meshes.btf150dz, tracerField, velocityField, T_init, Timing(18000, 3600, 8), linearUpwind, parallel, fast)

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
        build.add(self.btf300dzCubicFit)
        build.add(self.btf150dzLinearUpwind)
