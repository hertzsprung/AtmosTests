from ninjaopenfoam import GhostMesh, DeformationPlaneBuilder, DeformationPlaneCollated
import os

class DeformationPlane:
    def __init__(self, parallel, fast):
        fastMesh = GhostMesh('deformationPlane-mesh-fast', os.path.join('src/deformationPlane/mesh-fast'))

        meshUniform6 = GhostMesh('deformationPlane-mesh-uniform-6', os.path.join('src/deformationPlane/mesh-uniform-6'))
        meshUniform3 = GhostMesh('deformationPlane-mesh-uniform-3', os.path.join('src/deformationPlane/mesh-uniform-3'))
        meshUniform2 = GhostMesh('deformationPlane-mesh-uniform-2', os.path.join('src/deformationPlane/mesh-uniform-2'))
        meshUniform1_5 = GhostMesh('deformationPlane-mesh-uniform-1.5', os.path.join('src/deformationPlane/mesh-uniform-1.5'))
        meshUniform1 = GhostMesh('deformationPlane-mesh-uniform-1', os.path.join('src/deformationPlane/mesh-uniform-1'))
        meshUniform0_75 = GhostMesh('deformationPlane-mesh-uniform-0.75', os.path.join('src/deformationPlane/mesh-uniform-0.75'))
        meshUniform0_5 = GhostMesh('deformationPlane-mesh-uniform-0.5', os.path.join('src/deformationPlane/mesh-uniform-0.5'))
        meshUniform0_375 = GhostMesh('deformationPlane-mesh-uniform-0.375', os.path.join('src/deformationPlane/mesh-uniform-0.375'))

        meshDistorted6 = GhostMesh('deformationPlane-mesh-distorted-6', os.path.join('src/deformationPlane/mesh-distorted-6'))
        meshDistorted3 = GhostMesh('deformationPlane-mesh-distorted-3', os.path.join('src/deformationPlane/mesh-distorted-3'))
        meshDistorted2 = GhostMesh('deformationPlane-mesh-distorted-2', os.path.join('src/deformationPlane/mesh-distorted-2'))
        meshDistorted1_5 = GhostMesh('deformationPlane-mesh-distorted-1.5', os.path.join('src/deformationPlane/mesh-distorted-1.5'))
        meshDistorted1 = GhostMesh('deformationPlane-mesh-distorted-1', os.path.join('src/deformationPlane/mesh-distorted-1'))
        meshDistorted0_75 = GhostMesh('deformationPlane-mesh-distorted-0.75', os.path.join('src/deformationPlane/mesh-distorted-0.75'))
        meshDistorted0_5 = GhostMesh('deformationPlane-mesh-distorted-0.5', os.path.join('src/deformationPlane/mesh-distorted-0.5'))
        meshDistorted0_375 = GhostMesh('deformationPlane-mesh-distorted-0.375', os.path.join('src/deformationPlane/mesh-distorted-0.375'))

        self.meshes = [
                fastMesh,
                meshUniform6, meshUniform3, meshUniform2, meshUniform1_5,
                meshUniform1, meshUniform0_75, meshUniform0_5, meshUniform0_375,
                meshDistorted6, meshDistorted3, meshDistorted2, meshDistorted1_5,
                meshDistorted1, meshDistorted0_75, meshDistorted0_5, meshDistorted0_375
        ]

        deformationPlane = DeformationPlaneBuilder(
                parallel=parallel,
                fast=fast,
                fastMesh=fastMesh)

        self.uniformCubicFitCollated = deformationPlane.collated(
                'deformationPlane-uniform-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationPlane/cubicFit'),
                tests=[
                    DeformationPlaneCollated.Test('deformationPlane-uniform-6-cubicFit',     6,     meshUniform6,     timestep=0.01),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-3-cubicFit',     3,     meshUniform3,     timestep=0.005),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-2-cubicFit',     2,     meshUniform2,     timestep=0.004),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-1.5-cubicFit',   1.5,   meshUniform1_5,   timestep=0.0025),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-1-cubicFit',     1,     meshUniform1,     timestep=0.002),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.75-cubicFit',  0.75,  meshUniform0_75,  timestep=0.00125),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.5-cubicFit',   0.5,   meshUniform0_5,   timestep=0.001),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.375-cubicFit', 0.375, meshUniform0_375, timestep=0.000625)
                ])

        self.uniformHighOrderFitCollated = deformationPlane.collated(
                'deformationPlane-uniform-highOrderFit-collated',
                fvSchemes=os.path.join('src/deformationPlane/highOrderFit'),
                tests=[
                    DeformationPlaneCollated.Test('deformationPlane-uniform-6-highOrderFit',     6,     meshUniform6,     timestep=0.01),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-3-highOrderFit',     3,     meshUniform3,     timestep=0.005),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-2-highOrderFit',     2,     meshUniform2,     timestep=0.004),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-1.5-highOrderFit',   1.5,   meshUniform1_5,   timestep=0.0025),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-1-highOrderFit',     1,     meshUniform1,     timestep=0.002),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.75-highOrderFit',  0.75,  meshUniform0_75,  timestep=0.00125),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.5-highOrderFit',   0.5,   meshUniform0_5,   timestep=0.001),
                    DeformationPlaneCollated.Test('deformationPlane-uniform-0.375-highOrderFit', 0.375, meshUniform0_375, timestep=0.000625)
                ],
                controlDict=os.path.join('src/deformationPlane/controlDict.highOrderFit.template'),
                solverRule='scalarDeformationHighOrderFit')

        self.distortedCubicFitCollated = deformationPlane.collated(
                'deformationPlane-distorted-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationPlane/cubicFit'),
                tests=[
                    DeformationPlaneCollated.Test('deformationPlane-distorted-6-cubicFit',     6,     meshDistorted6,     timestep=0.01),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-3-cubicFit',     3,     meshDistorted3,     timestep=0.005),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-2-cubicFit',     2,     meshDistorted2,     timestep=0.004),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-1.5-cubicFit',   1.5,   meshDistorted1_5,   timestep=0.0025),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-1-cubicFit',     1,     meshDistorted1,     timestep=0.002),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.75-cubicFit',  0.75,  meshDistorted0_75,  timestep=0.00125),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.5-cubicFit',   0.5,   meshDistorted0_5,   timestep=0.001),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.375-cubicFit', 0.375, meshDistorted0_375, timestep=0.000625)
                ])

        self.distortedHighOrderFitCollated = deformationPlane.collated(
                'deformationPlane-distorted-highOrderFit-collated',
                fvSchemes=os.path.join('src/deformationPlane/highOrderFit'),
                tests=[
                    DeformationPlaneCollated.Test('deformationPlane-distorted-6-highOrderFit',     6,     meshDistorted6,     timestep=0.01),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-3-highOrderFit',     3,     meshDistorted3,     timestep=0.005),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-2-highOrderFit',     2,     meshDistorted2,     timestep=0.004),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-1.5-highOrderFit',   1.5,   meshDistorted1_5,   timestep=0.0025),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-1-highOrderFit',     1,     meshDistorted1,     timestep=0.002),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.75-highOrderFit',  0.75,  meshDistorted0_75,  timestep=0.00125),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.5-highOrderFit',   0.5,   meshDistorted0_5,   timestep=0.001),
                    DeformationPlaneCollated.Test('deformationPlane-distorted-0.375-highOrderFit', 0.375, meshDistorted0_375, timestep=0.000625)
                ],
                controlDict=os.path.join('src/deformationPlane/controlDict.highOrderFit.template'),
                solverRule='scalarDeformationHighOrderFit')

    def addTo(self, build):
        build.addAll(self.meshes)

        build.add(self.uniformCubicFitCollated)
        build.addAll(self.uniformCubicFitCollated.tests)
        build.add(self.uniformHighOrderFitCollated)
        build.addAll(self.uniformHighOrderFitCollated.tests)
        build.add(self.distortedCubicFitCollated)
        build.addAll(self.distortedCubicFitCollated.tests)
        build.add(self.distortedHighOrderFitCollated)
        build.addAll(self.distortedHighOrderFitCollated.tests)
