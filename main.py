from Resources.readInput import *
from quineMcCluskey import *

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput("Examples/input.txt")

    print("input", ' '.join(map(str, input))) 

    newImplicants = set()

    for element in input:
        newImplicants.update(element.unfold(readInput.stages))

    print("newImplicants", '\n'.join(map(str, newImplicants))) 

    output = QuineMcCluskey.execute(list(newImplicants))

    print(len(newImplicants))
    
    Resources.printOutput(newImplicants, output)

if __name__ == "__main__":
    main()