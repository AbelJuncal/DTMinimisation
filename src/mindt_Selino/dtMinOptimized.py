# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

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