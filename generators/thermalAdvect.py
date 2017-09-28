from ninjaopenfoam import Advect, Timing

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        cubicFit = os.path.join('src/schaerAdvect/cubicFit')

        self.btf300dzCubicFit = Advect('thermalAdvect-btf-300dz-cubicFit', 0, 250, meshes.btf300dz, tracerField, velocityField, Timing(18000, 3600, 8), cubicFit, parallel, fast)

    def addTo(self, build):
        build.add(self.btf300dzCubicFit)
