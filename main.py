from Resources.readInput import *
from quineMcCluskey import *

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput("Examples/input.txt")

    output = QuineMcCluskey.execute(input)

    newImplicants = []

    for element in input:
        print(element)
        element.unfold(element.list, readInput.stages)
    
    Resources.printOutput(input, output)

if __name__ == "__main__":
    main()