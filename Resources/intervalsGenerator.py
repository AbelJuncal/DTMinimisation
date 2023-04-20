import random
from Implicant.intervalmplicant import *

class IntervalsGenerator(object):
    @classmethod
    def generate(self, nVars = 3, maxnThres = 5, nImpl = 4):
        N = 100

        stages = list(range(0, N+1, int(N/maxnThres)))

        stagesList = []
        implicantList = []

        for _ in range (nVars):
            stagesList.append(stages)

        self.stages = stagesList

        for _ in range(nImpl):
            implicant = []
            for _ in range (nVars):
                num1, num2 = random.sample(range(1, N+1), 2)
                newTuple = (num1, num2)
                implicant.append(newTuple)
            implicantList.append(IntervalImplicant(implicant))

        return implicantList