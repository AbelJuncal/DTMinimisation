from mindt_Selino.Implicant.intervalmplicant import *

class optimizedIntervalImplicant(IntervalImplicant):
    def unfold(self, variableStage):
        newSteps = []

        for var in variableStage:
            newSteps.append(list(range(0, len(var))))

        unfolds = self.unfoldTuple(self.list, variableStage, newSteps)
        result = set()

        for imp in unfolds:
            result.add(IntervalImplicant(imp))

        return result
    
    def unfoldTuple(self, tuple, variableStage, newSteps):
        if(tuple==[]):
            yield []
        else:
            start = tuple[0][0]
            end = tuple[0][1]
            steps = variableStage[0]
            normalized = newSteps[0]
            i = steps.index(start)

            while steps[i]!=end:
                for imp in self.unfoldTuple(tuple[1:], variableStage[1:], newSteps[1:]):
                    yield [(normalized[i], normalized[i+1])]+imp
                i=i+1