from ninjaopenfoam import BlockMesh, CutCellMesh, RestingBuilder, RestingCollated, \
        SlantedCellMesh, TerrainFollowingMesh
import ninjaopenfoam as ninja

import os

class Resting:
    def __init__(self, parallel, fast):
        meshNoOrography = BlockMesh('resting-mesh-noOrography', os.path.join('src/resting/mesh-noOrography'))

        meshBtf1000m = TerrainFollowingMesh('resting-mesh-btf-1000m', meshNoOrography, os.path.join('src/resting/mesh-btf-1000m'))
        meshBtf2000m = TerrainFollowingMesh('resting-mesh-btf-2000m', meshNoOrography, os.path.join('src/resting/mesh-btf-2000m'))
        meshBtf3000m = TerrainFollowingMesh('resting-mesh-btf-3000m', meshNoOrography, os.path.join('src/resting/mesh-btf-3000m'))
        meshBtf4000m = TerrainFollowingMesh('resting-mesh-btf-4000m', meshNoOrography, os.path.join('src/resting/mesh-btf-4000m'))
        meshBtf5000m = TerrainFollowingMesh('resting-mesh-btf-5000m', meshNoOrography, os.path.join('src/resting/mesh-btf-5000m'))
        meshBtf6000m = TerrainFollowingMesh('resting-mesh-btf-6000m', meshNoOrography, os.path.join('src/resting/mesh-btf-6000m'))

        meshSleve1000m = TerrainFollowingMesh('resting-mesh-sleve-1000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-1000m'))
        meshSleve2000m = TerrainFollowingMesh('resting-mesh-sleve-2000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-2000m'))
        meshSleve3000m = TerrainFollowingMesh('resting-mesh-sleve-3000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-3000m'))
        meshSleve4000m = TerrainFollowingMesh('resting-mesh-sleve-4000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-4000m'))
        meshSleve5000m = TerrainFollowingMesh('resting-mesh-sleve-5000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-5000m'))
        meshSleve6000m = TerrainFollowingMesh('resting-mesh-sleve-6000m', meshNoOrography, os.path.join('src/resting/mesh-sleve-6000m'))

        createPatchDict = os.path.join('src/resting/createPatchDict')

        meshCutCell1000m = CutCellMesh('resting-mesh-cutCell-1000m', os.path.join('src/resting/mesh-cutCell-1000m'), createPatchDict)
        meshCutCell2000m = CutCellMesh('resting-mesh-cutCell-2000m', os.path.join('src/resting/mesh-cutCell-2000m'), createPatchDict)
        meshCutCell3000m = CutCellMesh('resting-mesh-cutCell-3000m', os.path.join('src/resting/mesh-cutCell-3000m'), createPatchDict)
        meshCutCell4000m = CutCellMesh('resting-mesh-cutCell-4000m', os.path.join('src/resting/mesh-cutCell-4000m'), createPatchDict)
        meshCutCell5000m = CutCellMesh('resting-mesh-cutCell-5000m', os.path.join('src/resting/mesh-cutCell-5000m'), createPatchDict)
        meshCutCell6000m = CutCellMesh('resting-mesh-cutCell-6000m', os.path.join('src/resting/mesh-cutCell-6000m'), createPatchDict)

        meshSlantedCell1000m = SlantedCellMesh('resting-mesh-slantedCell-1000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-1000m'))
        meshSlantedCell2000m = SlantedCellMesh('resting-mesh-slantedCell-2000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-2000m'))
        meshSlantedCell3000m = SlantedCellMesh('resting-mesh-slantedCell-3000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-3000m'))
        meshSlantedCell4000m = SlantedCellMesh('resting-mesh-slantedCell-4000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-4000m'))
        meshSlantedCell5000m = SlantedCellMesh('resting-mesh-slantedCell-5000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-5000m'))
        meshSlantedCell6000m = SlantedCellMesh('resting-mesh-slantedCell-6000m', meshNoOrography, os.path.join('src/resting/mesh-slantedCell-6000m'))

        self.meshes = [
                meshNoOrography,
                meshBtf1000m, meshBtf2000m, meshBtf3000m, meshBtf4000m, meshBtf5000m, meshBtf6000m,
                meshSleve1000m, meshSleve2000m, meshSleve3000m, meshSleve4000m, meshSleve5000m, meshSleve6000m,
                meshCutCell1000m, meshCutCell2000m, meshCutCell3000m, meshCutCell4000m, meshCutCell5000m, meshCutCell6000m,
                meshSlantedCell1000m, meshSlantedCell2000m, meshSlantedCell3000m, meshSlantedCell4000m, meshSlantedCell5000m, meshSlantedCell6000m
        ]

        # maxwByMountainHeight

        resting = RestingBuilder(parallel, fast, fastMesh=meshNoOrography)

        self.btfLinearUpwind = resting.collateByMountainHeight(
                'resting-btf-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-btf-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-btf-1000m-linearUpwind', 1000, meshBtf1000m, timestep=25),
                    RestingCollated.Test('resting-btf-2000m-linearUpwind', 2000, meshBtf2000m, timestep=25),
                    RestingCollated.Test('resting-btf-3000m-linearUpwind', 3000, meshBtf3000m, timestep=25),
                    RestingCollated.Test('resting-btf-4000m-linearUpwind', 4000, meshBtf4000m, timestep=25),
                    RestingCollated.Test('resting-btf-5000m-linearUpwind', 5000, meshBtf5000m, timestep=25),
                    RestingCollated.Test('resting-btf-6000m-linearUpwind', 6000, meshBtf6000m, timestep=25)
        ])

        self.btfCubicFit = resting.collateByMountainHeight(
                'resting-btf-cubicFit-collated',
                fvSchemes=os.path.join('src/resting/cubicFit'),
                tests=[
                    RestingCollated.Test('resting-btf-0m-cubicFit', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-btf-1000m-cubicFit', 1000, meshBtf1000m, timestep=25),
                    RestingCollated.Test('resting-btf-2000m-cubicFit', 2000, meshBtf2000m, timestep=25),
                    RestingCollated.Test('resting-btf-3000m-cubicFit', 3000, meshBtf3000m, timestep=25),
                    RestingCollated.Test('resting-btf-4000m-cubicFit', 4000, meshBtf4000m, timestep=25),
                    RestingCollated.Test('resting-btf-5000m-cubicFit', 5000, meshBtf5000m, timestep=25),
                    RestingCollated.Test('resting-btf-6000m-cubicFit', 6000, meshBtf6000m, timestep=25)
        ])

        self.sleveLinearUpwind = resting.collateByMountainHeight(
                'resting-sleve-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-sleve-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-sleve-1000m-linearUpwind', 1000, meshSleve1000m, timestep=25),
                    RestingCollated.Test('resting-sleve-2000m-linearUpwind', 2000, meshSleve2000m, timestep=25),
                    RestingCollated.Test('resting-sleve-3000m-linearUpwind', 3000, meshSleve3000m, timestep=25),
                    RestingCollated.Test('resting-sleve-4000m-linearUpwind', 4000, meshSleve4000m, timestep=25),
                    RestingCollated.Test('resting-sleve-5000m-linearUpwind', 5000, meshSleve5000m, timestep=25),
                    RestingCollated.Test('resting-sleve-6000m-linearUpwind', 6000, meshSleve6000m, timestep=25)
        ])

        self.sleveCubicFit = resting.collateByMountainHeight(
                'resting-sleve-cubicFit-collated',
                fvSchemes=os.path.join('src/resting/cubicFit'),
                tests=[
                    RestingCollated.Test('resting-sleve-0m-cubicFit', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-sleve-1000m-cubicFit', 1000, meshSleve1000m, timestep=25),
                    RestingCollated.Test('resting-sleve-2000m-cubicFit', 2000, meshSleve2000m, timestep=25),
                    RestingCollated.Test('resting-sleve-3000m-cubicFit', 3000, meshSleve3000m, timestep=25),
                    RestingCollated.Test('resting-sleve-4000m-cubicFit', 4000, meshSleve4000m, timestep=25),
                    RestingCollated.Test('resting-sleve-5000m-cubicFit', 5000, meshSleve5000m, timestep=25),
                    RestingCollated.Test('resting-sleve-6000m-cubicFit', 6000, meshSleve6000m, timestep=25)
        ])

        self.cutCellLinearUpwind = resting.collateByMountainHeight(
                'resting-cutCell-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-cutCell-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-cutCell-1000m-linearUpwind', 1000, meshCutCell1000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-2000m-linearUpwind', 2000, meshCutCell2000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-3000m-linearUpwind', 3000, meshCutCell3000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-4000m-linearUpwind', 4000, meshCutCell4000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-5000m-linearUpwind', 5000, meshCutCell5000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-6000m-linearUpwind', 6000, meshCutCell6000m, timestep=25)
        ])

        self.cutCellCubicFit = resting.collateByMountainHeight(
                'resting-cutCell-cubicFit-collated',
                fvSchemes=os.path.join('src/resting/cubicFit'),
                tests=[
                    RestingCollated.Test('resting-cutCell-0m-cubicFit', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-cutCell-1000m-cubicFit', 1000, meshCutCell1000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-2000m-cubicFit', 2000, meshCutCell2000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-3000m-cubicFit', 3000, meshCutCell3000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-4000m-cubicFit', 4000, meshCutCell4000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-5000m-cubicFit', 5000, meshCutCell5000m, timestep=25),
                    RestingCollated.Test('resting-cutCell-6000m-cubicFit', 6000, meshCutCell6000m, timestep=25)
        ])

        self.slantedCellLinearUpwind = resting.collateByMountainHeight(
                'resting-slantedCell-linearUpwind-collated',
                fvSchemes=os.path.join('src/resting/linearUpwind'),
                tests=[
                    RestingCollated.Test('resting-slantedCell-0m-linearUpwind', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-slantedCell-1000m-linearUpwind', 1000, meshSlantedCell1000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-2000m-linearUpwind', 2000, meshSlantedCell2000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-3000m-linearUpwind', 3000, meshSlantedCell3000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-4000m-linearUpwind', 4000, meshSlantedCell4000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-5000m-linearUpwind', 5000, meshSlantedCell5000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-6000m-linearUpwind', 6000, meshSlantedCell6000m, timestep=25)
        ])

        self.slantedCellCubicFit = resting.collateByMountainHeight(
                'resting-slantedCell-cubicFit-collated',
                fvSchemes=os.path.join('src/resting/cubicFit'),
                tests=[
                    RestingCollated.Test('resting-slantedCell-0m-cubicFit', 0, meshNoOrography, timestep=25),
                    RestingCollated.Test('resting-slantedCell-1000m-cubicFit', 1000, meshSlantedCell1000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-2000m-cubicFit', 2000, meshSlantedCell2000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-3000m-cubicFit', 3000, meshSlantedCell3000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-4000m-cubicFit', 4000, meshSlantedCell4000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-5000m-cubicFit', 5000, meshSlantedCell5000m, timestep=25),
                    RestingCollated.Test('resting-slantedCell-6000m-cubicFit', 6000, meshSlantedCell6000m, timestep=25)
        ])

    def addTo(self, build):
        build.addAll(self.meshes)
        build.add(self.btfLinearUpwind)
        build.addAll(self.btfLinearUpwind.tests)
        build.add(self.sleveLinearUpwind)
        build.addAll(self.sleveLinearUpwind.tests)
        build.add(self.cutCellLinearUpwind)
        build.addAll(self.cutCellLinearUpwind.tests)
        build.add(self.slantedCellLinearUpwind)
        build.addAll(self.slantedCellLinearUpwind.tests)
        build.add(self.btfCubicFit)
        build.addAll(self.btfCubicFit.tests)
        build.add(self.sleveCubicFit)
        build.addAll(self.sleveCubicFit.tests)
        build.add(self.cutCellCubicFit)
        build.addAll(self.cutCellCubicFit.tests)
        build.add(self.slantedCellCubicFit)
        build.addAll(self.slantedCellCubicFit.tests)
