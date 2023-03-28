class Implicant():
    def matches(otherImplicant):
        raise "This class is not intended to be instantiated"
    
class BooleanImplicant(Implicant):
    def __init__(self, string):
        self.string = string

    def matches(self, otherImplicant):
    
        difference = 0
        merging = ""

        for z in range(len(self.string)):
            if self.string[z] == otherImplicant.string[z]:
                merging = merging + self.string[z]
            else:
                merging = merging + "-"
                difference+=1

        if(difference == 1):
            return BooleanImplicant(merging)
        
        return None

    def __str__ (self):
        return self.string
    
class QuineMcCluskey(object):
    @classmethod
    def execute(self, input):

        output = set()

        while(input):
            auxInput = Resources.listToDictionary(input)
            mergingList = []

            for i in range(0, len(input)-1):
                for j in range(i+1, len(input)):
                    first = input[i]
                    second = input[j]

                    fusion = first.matches(second)
                    
                    if fusion:
                        mergingList.append(fusion)
                        auxInput[first]=1
                        auxInput[second]=1

            output.update(Resources.primeImplicants(auxInput))
            
            input = mergingList

        return output
    
class ReadInput():
    @classmethod
    def readBooleanInput(self, filename):
        file = open(filename)
        lines = file.read().splitlines()
        input = []

        for line in lines:
            implicant = BooleanImplicant(line)
            input.append(implicant)

        return input
    
    @classmethod
    def readIntervalInput(self, filename):
        file = open(filename)
        lines = file.read().splitlines()
        input = []
        
        numVariables = int(lines[0])
        lines.pop(0)

        setsList = []

        for i in range(numVariables):
            nuevoSetVariable = set()
            nuevoSetVariable.update([0, int(lines[0])])
            lines.pop(0)
            setsList.append(nuevoSetVariable)

        for element in lines:
            x = element.split()
            tuples = [] 
            nueva_lista = [x[i:i+2] for i in range(0, len(x), 2)]

            for i in range(numVariables):
                lista = nueva_lista[i]
                nuevatupler = []

                for elementer in lista:
                    setsList[i].add(int(elementer))
                    nuevatupler.append(int(elementer))

                nuevatupler = tuple(nuevatupler)
                tuples.append(nuevatupler)
            
            input.append(tuples)

        for i in range(numVariables):
            setordenado = sorted(setsList[i])
            setsList[i] = setordenado

        self.stages = setsList

        return input

class Resources(object):
    
    @classmethod
    def primeImplicants(self, dicImplicants):
        primeList = []
        for x , y in dicImplicants.items():
            if y == 0:
                primeList.append(x)

        return primeList

    @classmethod
    def printOutput(self, input, output):
        print("input", ' '.join(map(str, input))) 
        print("output", ' '.join(map(str, output)))

    @classmethod
    def listToDictionary(self, list):
        dict = {}

        for element in list:
            dict[element] = 0

        return dict

def main():

    #input = Resources.readBooleanInput("Examples/booleanExample1.txt")

    #output = QuineMcCluskey.execute(input)

    #Resources.printOutput(input, output)

    aux_input = ReadInput.readIntervalInput("Examples/input.txt")

    print(aux_input)




if __name__ == "__main__":
    main()