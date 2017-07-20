#!/usr/bin/python3

import configparser
import errno
import itertools
import ninja.gen
import ninja.model
import os

class AtmosTests:
    def __init__(self):
        config = configparser.ConfigParser()
        with open('build.properties', 'r') as f:
            config.read_file(itertools.chain(['[default]'], f))
            self.parallel = config['default']['solver_execution'] == 'parallel'

        self.build = ninja.model.Build()
        self.solvers()
        self.deformationSphere()
        self.schaerAdvect()

    def write(self):
        self.build.write()

    def solvers(self):
        advectionFoam = ninja.model.Solver(
                'advectionFoam',
                'advectionFoam -case $case -heun2',
                self.parallel)

        sphericalAdvectionFoam = ninja.model.Solver(
                'sphericalAdvectionFoam',
                'sphericalAdvectionFoam -case $case -heun2',
                self.parallel)

        self.build.add(advectionFoam)
        self.build.add(sphericalAdvectionFoam)

    def deformationSphere(self):
        b = self.build

        meshHex4 = ninja.model.GeodesicHexMesh('deformationSphere-mesh-hex-4', 4)
        meshHex8 = ninja.model.GeodesicHexMesh('deformationSphere-mesh-hex-8', 8)

        gaussiansHex4linearUpwind = ninja.model.DeformationSphere(
                'deformationSphere-gaussians-hex-4-linearUpwind',
                meshHex4,
                timestep=3200,
                fvSchemes=os.path.join('src', 'schaerAdvect', 'linearUpwind'),
                tracerFieldDict = os.path.join('src', 'deformationSphere', 'gaussians'),
                parallel=self.parallel)

        gaussiansHex8cubicFit = ninja.model.DeformationSphere(
                'deformationSphere-gaussians-hex-8-cubicFit',
                meshHex8,
                timestep=200,
                fvSchemes=os.path.join('src', 'deformationSphere', 'cubicFit'),
                tracerFieldDict = os.path.join('src', 'deformationSphere', 'gaussians'),
                parallel=self.parallel)

        b.add(meshHex4)
        b.add(meshHex8)
        b.add(gaussiansHex4linearUpwind)
        b.add(gaussiansHex8cubicFit)

    def schaerAdvect(self):
        b = self.build

        meshNoOrography = ninja.model.BlockMesh(
                'schaerAdvect-mesh-noOrography',
                os.path.join('src', 'schaerAdvect', 'mesh-noOrography'))

        meshBtf = ninja.model.TerrainFollowingMesh(
                'schaerAdvect-mesh-btf',
                meshNoOrography,
                os.path.join('src', 'schaerAdvect', 'mesh-btf'))

        noOrographyLinearUpwind = ninja.model.SchaerAdvect(
                'schaerAdvect-noOrography-linearUpwind',
                meshNoOrography,
                timestep=8,
                fvSchemes=os.path.join('src', 'schaerAdvect', 'linearUpwind'),
                parallel=self.parallel)

        b.add(meshNoOrography)
        b.add(meshBtf)
        b.add(noOrographyLinearUpwind)


if __name__ == '__main__':
    AtmosTests().write()
