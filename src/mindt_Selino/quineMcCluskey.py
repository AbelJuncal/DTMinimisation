# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from mindt_Selino.Resources.resources import *

class QuineMcCluskey(object):
    @classmethod
    def execute(self, input):

        output = set()

        while(input):
            auxInput = {element: 0 for element in input}
            mergingSet = set()

            for i in range(0, len(input)-1):
                for j in range(i+1, len(input)):
                    first = input[i]
                    second = input[j]

                    fusion = first.matches(second)
                    
                    if fusion is not None:
                        mergingSet.add(fusion)
                        auxInput[first]=1
                        auxInput[second]=1

            output.update(Resources.primeImplicants(auxInput))
            
            input = list(mergingSet)

        return output