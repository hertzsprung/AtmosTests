from ninjaopenfoam import GhostMesh	
import os

class DeformationPlane:
    def __init__(self, parallel, fast):
        fastMesh = GhostMesh('deformationPlane-mesh-fast', os.path.join('src/deformationPlane/mesh-fast'))

        self.meshes = [fastMesh]

    def addTo(self, build):
        build.addAll(self.meshes)
