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

def primeImplicants(dicImplicants):
    primeList = []
    for x , y in dicImplicants.items():
        if y == 0:
            primeList.append(x)

    return primeList

def stringApproach(input):

    output = set()

    while(input):
        auxInput = listToDictionary(input)
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

        output.update(primeImplicants(auxInput))
        
        input = mergingList

    return output

def printOutput(input, output):
    print("input", ' '.join(map(str, input))) 
    print("output", ' '.join(map(str, output)))


def listToDictionary(list):
    dict = {}

    for element in list:
        dict[element] = 0

    return dict

def readBooleanInput(filename):
    file = open(filename)
    lines = file.read().splitlines()
    input = []

    for line in lines:
        implicant = BooleanImplicant(line)
        input.append(implicant)

    return input

def main():
    #input = [BooleanImplicant("001"),BooleanImplicant("101"), BooleanImplicant("110"), BooleanImplicant("111")]

    input = readBooleanInput("Examples/booleanExample1.txt")

    output = stringApproach(input)

    printOutput(input, output)




if __name__ == "__main__":
    main()