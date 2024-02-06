from mindt_Selino.dtMinimisation import *
from mindt_Selino.optimizedQuineMcCluskey import OptimizedQuineMcCluskey

class DtMinOptimized(DtMinimisation):
    def __init__(self, path):
        readInput = ReadInput()

        input = readInput.readOptimizedIntervalInput(path)

        newImplicants = set()

        for element in input:
            newImplicants.update(element.unfold(readInput.stages))

        staggeredImplicants = list(newImplicants)

        output = OptimizedQuineMcCluskey.execute(staggeredImplicants, readInput.stages)

        self.input = input
        self.staggeredImplicants = staggeredImplicants
        self.output = list(output)