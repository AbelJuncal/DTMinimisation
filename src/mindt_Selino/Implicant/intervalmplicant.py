from mindt_Selino.Implicant.implicant import *

class IntervalImplicant(Implicant):
    def __init__(self, list):
        self.list = list

    def matches(self, otherImplicant):

        difference = 0
        merging = []

        for v in range(len(self.list)):
                    a, b = self.list[v]
                    c, d = otherImplicant.list[v]

                    if b >= c and a <= d:
                        interval = (min(a,c), max(b, d))
                        merging.append(interval)
                        if a != c or b != d:
                            difference += 1
                    else:
                        return None

        if difference == 1:
            return IntervalImplicant(merging)
    
        return None
    
    def unfold(self, variableStage):
        unfolds = self.unfoldTuple(self.list, variableStage)
        result = set()

        for imp in unfolds:
            result.add(IntervalImplicant(imp))

        return result
    
    def unfoldTuple(self, tuple, variableStage):
        if(tuple==[]):
            yield []
        else:
            start = tuple[0][0]
            end = tuple[0][1]
            steps = variableStage[0]
            i = steps.index(start)

            while steps[i]!=end:
                for imp in self.unfoldTuple(tuple[1:], variableStage[1:]):
                    yield [(steps[i], steps[i+1])]+imp
                i=i+1
    
    def __str__ (self):
        return f'{str(self.list)}'

    def __hash__ (self):
        return hash(str(self.list))

    def __eq__ (self, other) -> bool:
        return self.list == other.list