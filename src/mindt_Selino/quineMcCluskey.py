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