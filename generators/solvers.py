from ninjaopenfoam import SolverRule

class Solvers:
    def __init__(self, parallel):
        self.advectionFoam = SolverRule(
                'advectionFoam',
                'advectionFoam -case $case -heun2',
                parallel)

        self.advectionFoamRK4 = SolverRule(
                'advectionFoamRK4',
                'advectionFoam -case $case -rk4',
                parallel)

        self.advectionFoamHighOrderFit = SolverRule(
                'advectionFoamHighOrderFit',
                'advectionFoamHighOrderFit -case $case',
                parallel)

        self.advectiveFoamF = SolverRule(
                'advectiveFoamF',
                'advectiveFoamF -case $case',
                parallel)

        self.sphericalAdvectionFoam = SolverRule(
                'sphericalAdvectionFoam',
                'sphericalAdvectionFoam -case $case -heun2',
                parallel)

        self.exnerFoamH = SolverRule(
                'exnerFoamH',
                'exnerFoamH -case $case',
                parallel)

        self.exnerFoamCP = SolverRule(
                'exnerFoamCP',
                'exnerFoamCPinterpGrad -case $case',
                parallel)

    def addTo(self, build):
        build.add(self.advectionFoam)
        build.add(self.advectionFoamRK4)
        build.add(self.advectionFoamHighOrderFit)
        build.add(self.advectiveFoamF)
        build.add(self.sphericalAdvectionFoam)
        build.add(self.exnerFoamH)
        build.add(self.exnerFoamCP)
