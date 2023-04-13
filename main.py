from Resources.readInput import *
from quineMcCluskey import *

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput("Examples/input.txt")

    output = QuineMcCluskey.execute(input)

    newImplicants = []

    for element in input:
        print("PARA EL IMP", element)
        for imp in element.unfold(element.list, readInput.stages):
            print(imp)
    
    Resources.printOutput(input, output)

    Resources.examplesGenerator()

if __name__ == "__main__":
    main()