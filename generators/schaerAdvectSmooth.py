from ninjaopenfoam import SchaerAdvectBuilder, SchaerAdvectCollated
import os

class SchaerAdvectSmooth:
    def __init__(self, advect, parallel, fast):
        schaerAdvectCos4 = SchaerAdvectBuilder(
                mountainHeight=3000,
                tracerField=os.path.join('src/schaerAdvectSmooth/cos4TracerField'),
                velocityField=os.path.join('src/schaerAdvectSmooth/velocityField'),
                parallel=parallel,
                fast=fast,
                fastMesh=advect.meshNoOrography5000)

        self.cos4BtfCubicFitCollated = schaerAdvectCos4.collated(
                'schaerAdvectSmooth-cos4-btf-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-5000-cubicFit', 5000,     advect.meshBtf5000_3000m, timestep=80),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-2500-cubicFit', 2500,     advect.meshBtf2500_3000m, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-2000-cubicFit', 2000,     advect.meshBtf2000_3000m, timestep=25),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-1250-cubicFit', 1250,     advect.meshBtf1250_3000m, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-1000-cubicFit', 1000,     advect.meshBtf1000_3000m, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-667-cubicFit',  1000/3*2, advect.meshBtf667_3000m,  timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-500-cubicFit',  500,      advect.meshBtf500_3000m,  timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-333-cubicFit',  1000/3,   advect.meshBtf333_3000m,  timestep=5),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-250-cubicFit',  250,      advect.meshBtf250_3000m,  timestep=4)
                ],
                solverRule='advectionFoamRK4'
        )

        self.cos4BtfHighOrderFitCollated = schaerAdvectCos4.collated(
                'schaerAdvectSmooth-cos4-btf-highOrderFit-collated',
                fvSchemes=os.path.join('src/schaerAdvectSmooth/highOrderFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-5000-highOrderFit', 5000,     advect.meshBtf5000_3000m, timestep=80),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-2500-highOrderFit', 2500,     advect.meshBtf2500_3000m, timestep=40),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-2000-highOrderFit', 2000,     advect.meshBtf2000_3000m, timestep=25),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-1250-highOrderFit', 1250,     advect.meshBtf1250_3000m, timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-1000-highOrderFit', 1000,     advect.meshBtf1000_3000m, timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-667-highOrderFit',  1000/3*2, advect.meshBtf667_3000m,  timestep=10),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-500-highOrderFit',  500,      advect.meshBtf500_3000m,  timestep=8),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-btf-333-highOrderFit',  1000/3,   advect.meshBtf333_3000m,  timestep=5),
                ],
                controlDict=os.path.join('src/controlDict.highOrderFit.template'),
                solverRule='advectionFoamHighOrderFit'
        )

        self.cos4CutCellCubicFitCollated = schaerAdvectCos4.collated(
                'schaerAdvectSmooth-cos4-cutCell-cubicFit-collated',
                fvSchemes=os.path.join('src/schaerAdvect/cubicFit'),
                tests=[
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-5000-cubicFit', 5000,     advect.meshCutCell5000_3000m, timestep=200),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-2500-cubicFit', 2500,     advect.meshCutCell2500_3000m, timestep=80),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-2000-cubicFit', 2000,     advect.meshCutCell2000_3000m, timestep=50),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-1250-cubicFit', 1250,     advect.meshCutCell1250_3000m, timestep=50),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-1000-cubicFit', 1000,     advect.meshCutCell1000_3000m, timestep=50),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-667-cubicFit',  1000/3*2, advect.meshCutCell667_3000m,  timestep=25),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-500-cubicFit',  500,      advect.meshCutCell500_3000m,  timestep=20),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-333-cubicFit',  1000/3,   advect.meshCutCell333_3000m,  timestep=16),
                    SchaerAdvectCollated.Test('schaerAdvectSmooth-cos4-cutCell-250-cubicFit',  250,      advect.meshCutCell250_3000m,  timestep=10)
                ],
                solverRule='advectionFoamRK4'
        )

    def addTo(self, build):
        build.add(self.cos4BtfCubicFitCollated)
        build.addAll(self.cos4BtfCubicFitCollated.tests)
        build.add(self.cos4BtfHighOrderFitCollated)
        build.addAll(self.cos4BtfHighOrderFitCollated.tests)
        build.add(self.cos4CutCellCubicFitCollated)
        build.addAll(self.cos4CutCellCubicFitCollated.tests)
