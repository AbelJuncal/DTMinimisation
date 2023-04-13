from Resources.readInput import *
from quineMcCluskey import *

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput("Examples/input.txt")

    print("input", ' '.join(map(str, input))) 

    newImplicants = []

    for element in input:
        newImplicants.extend(element.stagger(readInput.stages))

    print("newImplicants", ' '.join(map(str, newImplicants))) 

    output = QuineMcCluskey.execute(newImplicants)
    
    Resources.printOutput(newImplicants, output)

if __name__ == "__main__":
    main()