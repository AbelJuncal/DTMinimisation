import math
import random
from Implicant.intervalmplicant import *

class IntervalsGenerator(object):
    @classmethod
    def generate(self, nVars = 3, maxnThres = 15, nImpl = 14):
        N = 100

        stagesList = []
        implicantList = []

        for _ in range (nVars):
            numStages = random.randint(2, maxnThres)
            stages = list(range(0, N+1, math.ceil(N/numStages)))

            if(len(stages)==numStages):
                stages.append(100)
            stagesList.append(stages)

        self.stages = stagesList

        for _ in range(nImpl):
            implicant = []
            for v in range (nVars):
                sample = random.sample(stagesList[v], 2)
                implicant.append((min(sample), max(sample)))
            implicantList.append(IntervalImplicant(implicant))

        return implicantList