from ninjaopenfoam import Advect

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        linearUpwind = os.path.join('src/schaerAdvect/linearUpwind')

        self.btf300dzLinearUpwind = Advect('thermalAdvect-btf-300dz-linearUpwind', 0, 250, meshes.btf300dz, tracerField, velocityField, 8, linearUpwind, parallel, fast)

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
