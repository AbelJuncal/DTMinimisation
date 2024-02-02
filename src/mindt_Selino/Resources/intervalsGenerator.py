import math
import random
from mindt_Selino.Implicant.intervalmplicant import *

class IntervalsGenerator(object):
    @classmethod
    def generate(self, nVars = 3, maxnThres = 15, nImpl = 14):
        N = 100

        stagesList = []
        implicantList = []

        maxStages = 0

        for _ in range (nVars):
            numStages = random.randint(2, maxnThres)

            stages = list(range(0, N+1, math.ceil(N/numStages)))

            if(len(stages)==numStages):
                stages.append(100)
            stagesList.append(stages)

            if(len(stages)-1 > maxStages):
                maxStages = len(stages)-1

        self.stages = stagesList
        self.maxStages = maxStages

        for _ in range(nImpl):
            implicant = []
            for v in range (nVars):
                sample = random.sample(stagesList[v], 2)
                implicant.append((min(sample), max(sample)))
            implicantList.append(IntervalImplicant(implicant))

        return implicantList