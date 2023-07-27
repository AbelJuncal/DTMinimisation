from quineMcCluskey import *
from Implicant.intervalmplicant import *

class OptimizedQuineMcCluskey(QuineMcCluskey):
    @classmethod
    def execute(self, input, inputStages):

        # groups = {}

        # #hago los grupos
        # for i in range(0, len(input)-1):
            
        #     implicant = input[i]

        #     sum = 0

        #     for interval in implicant.list:
        #         sum = sum + interval[0]

        #     if sum in groups:
        #         groups[sum].append(implicant)
        #     else:
        #         groups[sum] = [implicant]

        # myKeys = list(groups.keys())
        # myKeys.sort()
        # sorted_dict = {i: groups[i] for i in myKeys}

        # #Hasta aquí todo bien, hay que fusionar os que poden machear

        # maxDiff = max(len(sub) for sub in inputStages) - 1

        # items = list(sorted_dict.items())

        # for i in range(len(items)-1):
        #     clave_actual, valor_actual = items[i]
        #     mergeList = valor_actual
        #     for j in range(i+1, len(items)):
        #         clave_siguiente, valor_siguiente = items[j]

        #         if(abs(clave_actual-clave_siguiente)<=maxDiff):
        #             mergeList.append(valor_siguiente)

        #Calculamos suma de mínimos

        input_sumas = []

        for implicant in input:
            minimal_sum = 0

            minimal_sum = sum(interval[0] for interval in implicant.list)
            
            input_sumas.append((minimal_sum, implicant))

        input_sumas.sort(key=lambda x: x[0])

        #Calculamos diferencia máxima

        maxDiff = max(len(sub) for sub in inputStages) - 1

        input = input_sumas   

        output = set()

        while(input):
            auxInput = {element[1]: 0 for element in input}
            mergingSet = set()

            for i in range(0, len(input)-1):
                for j in range(i+1, len(input)):
                    first_sum = input[i][0]
                    second_sum = input[j][0]
                    
                    if(abs(first_sum-second_sum)>maxDiff):
                        break
                        
                    first = input[i][1]
                    second = input[j][1]

                    fusion = first.matches(second)
                        
                    if fusion is not None:
                        minimal_sum = 0
                        minimal_sum = sum(interval[0] for interval in fusion.list)

                        mergingSet.add((minimal_sum, fusion))
                        auxInput[first]=1
                        auxInput[second]=1

            output.update(Resources.primeImplicants(auxInput))
            
            input = list(mergingSet)
            input.sort(key=lambda x: x[0])

        auxOutput = set()

        #"Desnormalizar" os resultados
        auxOutput = []

        for implicant in list(output):
            var = 0
            auxImplicant = []
            for interval in implicant.list:
                auxImplicant.append((inputStages[var][interval[0]], inputStages[var][interval[1]]))
                var= var+1
            auxOutput.append(IntervalImplicant(auxImplicant))

        return auxOutput