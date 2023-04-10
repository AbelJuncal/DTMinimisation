from Implicant.implicant import *

class IntervalImplicant(Implicant):
    def __init__(self, list):
        self.list = list

    def matches(self, otherImplicant):

        difference = 0
        merging = []

        for z in range(len(self.list)):

            if isinstance(self.list[z] , tuple):
                if isinstance(otherImplicant.list[z] , tuple):
                    if self.list[z][0] == otherImplicant.list[z][0] and self.list[z][1] == otherImplicant.list[z][1]:
                        merging.append(self.list[z])
                    elif self.list[z][1] >= otherImplicant.list[z][0] and self.list[z][0] <= otherImplicant.list[z][1]:
                        interval = (min(self.list[z][0],otherImplicant.list[z][0]), max(self.list[z][1], otherImplicant.list[z][1]))
                        merging.append(interval)
                        difference += 1
                    else:
                        return None

        if difference == 1:
            return IntervalImplicant(merging)
    
        return None
    
    def unfold(self, tuple, variableStage):
        if(tuple==[]):
            yield []
        else:
            start = tuple[0][0]
            end = tuple[0][1]
            steps=variableStage[0]
            i = steps.index(start)

            while steps[i]!=end:
                i=i+1
                for imp in self.unfold(tuple[1:], variableStage[1:]):
                    yield [(steps[i], steps[i+1])]+imp
    
    def __str__ (self):
        return str(self.list)