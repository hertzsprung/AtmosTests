import ninjaopenfoam as ninja

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        cubicFit = os.path.join('src/schaerAdvect/cubicFit')
        T_init = os.path.join('src/schaerWaves/theta_init')

        self.btf500dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-500dz-cubicFit', 833.33333, meshes.btf500dz, 13.33333333, cubicFit, parallel, fast, meshes.btfFast)
        self.btf300dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-300dz-cubicFit', 500, meshes.btf300dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf250dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-250dz-cubicFit', 416.66667, meshes.btf250dz, 6.66666666, cubicFit, parallel, fast, meshes.btfFast)
        self.btf200dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-200dz-cubicFit', 333.33333, meshes.btf200dz, 5.333333333, cubicFit, parallel, fast, meshes.btfFast)
        self.btf150dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-150dz-cubicFit', 250, meshes.btf150dz, 4.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf125dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-125dz-cubicFit', 208.33333, meshes.btf125dz, 3.333333333, cubicFit, parallel, fast, meshes.btfFast)
        self.btf100dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-100dz-cubicFit', 166.66667, meshes.btf100dz, 2.666666667, cubicFit, parallel, fast, meshes.btfFast)
        self.btf75dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-75dz-cubicFit', 125, meshes.btf75dz, 2.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf50dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-50dz-cubicFit', 83.33333, meshes.btf50dz, 1.333333333, cubicFit, parallel, fast, meshes.btfFast)

    def addTo(self, build):
        build.add(self.btf500dzCubicFit)
        build.add(self.btf300dzCubicFit)
        build.add(self.btf250dzCubicFit)
        build.add(self.btf200dzCubicFit)
        build.add(self.btf150dzCubicFit)
        build.add(self.btf125dzCubicFit)
        build.add(self.btf100dzCubicFit)
        build.add(self.btf75dzCubicFit)
        build.add(self.btf50dzCubicFit)
