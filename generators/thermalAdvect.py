import ninjaopenfoam as ninja

import os

class ThermalAdvect:
    def __init__(self, meshes, parallel, fast):
        tracerField = os.path.join('src/thermalAdvect/tracerField')
        velocityField = os.path.join('src/thermalAdvect/velocityField')
        cubicFit = os.path.join('src/schaerAdvect/cubicFit')
        T_init = os.path.join('src/schaerWaves/theta_init')

        self.btf500dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-500dz-cubicFit', 833.33333, meshes.btf500dz, 25, cubicFit, parallel, fast, meshes.btfFast)
        self.btf300dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-300dz-cubicFit', 500, meshes.btf300dz, 16.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf250dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-250dz-cubicFit', 416.66667, meshes.btf250dz, 12, cubicFit, parallel, fast, meshes.btfFast)
        self.btf200dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-200dz-cubicFit', 333.33333, meshes.btf200dz, 10, cubicFit, parallel, fast, meshes.btfFast)
        self.btf150dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-150dz-cubicFit', 250, meshes.btf150dz, 8.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf125dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-125dz-cubicFit', 208.33333, meshes.btf125dz, 6.666666667, cubicFit, parallel, fast, meshes.btfFast)
        self.btf100dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-100dz-cubicFit', 166.66667, meshes.btf100dz, 5.333333333, cubicFit, parallel, fast, meshes.btfFast)
        self.btf75dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-75dz-cubicFit', 125, meshes.btf75dz, 4.0, cubicFit, parallel, fast, meshes.btfFast)
        self.btf50dzCubicFit = ninja.ThermalAdvect('thermalAdvect-btf-50dz-cubicFit', 83.33333, meshes.btf50dz, 2.666666667, cubicFit, parallel, fast, meshes.btfFast)

        self.cutCell500dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-500dz-cubicFit', 833.33333, meshes.cutCell500dz, 25, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell300dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-300dz-cubicFit', 500, meshes.cutCell300dz, 16.0, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell250dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-250dz-cubicFit', 416.66667, meshes.cutCell250dz, 10, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell200dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-200dz-cubicFit', 333.33333, meshes.cutCell200dz, 5.333333333, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell150dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-150dz-cubicFit', 250, meshes.cutCell150dz, 0.5, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell125dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-125dz-cubicFit', 208.33333, meshes.cutCell125dz, 3, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell100dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-100dz-cubicFit', 166.66667, meshes.cutCell100dz, 0.2, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell75dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-75dz-cubicFit', 125, meshes.cutCell75dz, 1.0, cubicFit, parallel, fast, meshes.btfFast)
        self.cutCell50dzCubicFit = ninja.ThermalAdvect('thermalAdvect-cutCell-50dz-cubicFit', 83.33333, meshes.cutCell50dz, 0.25, cubicFit, parallel, fast, meshes.btfFast)

        self.slantedCell500dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-500dz-cubicFit', 833.33333, meshes.slantedCell500dz, 25, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell300dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-300dz-cubicFit', 500, meshes.slantedCell300dz, 10.0, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell250dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-250dz-cubicFit', 416.66667, meshes.slantedCell250dz, 8, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell200dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-200dz-cubicFit', 333.33333, meshes.slantedCell200dz, 6.66666667, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell150dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-150dz-cubicFit', 250, meshes.slantedCell150dz, 5.33333333, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell125dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-125dz-cubicFit', 208.33333, meshes.slantedCell125dz, 4, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell100dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-100dz-cubicFit', 166.66667, meshes.slantedCell100dz, 3.33333333, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell75dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-75dz-cubicFit', 125, meshes.slantedCell75dz, 2.66666667, cubicFit, parallel, fast, meshes.btfFast)
        self.slantedCell50dzCubicFit = ninja.ThermalAdvect('thermalAdvect-slantedCell-50dz-cubicFit', 83.33333, meshes.slantedCell50dz, 1.5, cubicFit, parallel, fast, meshes.btfFast)

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

        build.add(self.cutCell500dzCubicFit)
        build.add(self.cutCell300dzCubicFit)
        build.add(self.cutCell250dzCubicFit)
        build.add(self.cutCell200dzCubicFit)
        build.add(self.cutCell150dzCubicFit)
        build.add(self.cutCell125dzCubicFit)
        build.add(self.cutCell100dzCubicFit)
        build.add(self.cutCell75dzCubicFit)
        build.add(self.cutCell50dzCubicFit)

        build.add(self.slantedCell500dzCubicFit)
        build.add(self.slantedCell300dzCubicFit)
        build.add(self.slantedCell250dzCubicFit)
        build.add(self.slantedCell200dzCubicFit)
        build.add(self.slantedCell150dzCubicFit)
        build.add(self.slantedCell125dzCubicFit)
        build.add(self.slantedCell100dzCubicFit)
        build.add(self.slantedCell75dzCubicFit)
        build.add(self.slantedCell50dzCubicFit)
