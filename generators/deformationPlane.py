from ninjaopenfoam import GhostMesh, DeformationPlaneBuilder, DeformationPlaneCollated
import os

class DeformationPlane:
    def __init__(self, parallel, fast):
        fastMesh = GhostMesh('deformationPlane-mesh-fast', os.path.join('src/deformationPlane/mesh-fast'))
        meshUniform3 = GhostMesh('deformationPlane-mesh-uniform-3', os.path.join('src/deformationPlane/mesh-uniform-3'))

        self.meshes = [fastMesh, meshUniform3]

        deformationPlane = DeformationPlaneBuilder(
                parallel=parallel,
                fast=fast,
                fastMesh=fastMesh)

        self.uniformCubicFitCollated = deformationPlane.collated(
                'deformationPlane-uniform-cubicFit-collated',
                fvSchemes=os.path.join('src/deformationPlane/cubicFit'),
                tests=[
                    DeformationPlaneCollated.Test('deformationPlane-uniform-3-cubicFit', 3, meshUniform3, timestep=0.004)
                ])

    def addTo(self, build):
        build.addAll(self.meshes)

        build.add(self.uniformCubicFitCollated)
        build.addAll(self.uniformCubicFitCollated.tests)
