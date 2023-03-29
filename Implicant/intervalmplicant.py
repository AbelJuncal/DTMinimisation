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
                    else:
                        merging.append("-")
                        difference += 1
            else:
                if otherImplicant.list[z] == "-":
                    merging.append("-")

        if difference == 1:
            return IntervalImplicant(merging)
    
        return None
    
    def __str__ (self):
        return str(self.list)