from Resources.readInput import *
from quineMcCluskey import *

def main():

    input = ReadInput.readIntervalInput("Examples/input3.txt")

    output = QuineMcCluskey.execute(input)
    
    Resources.printOutput(input, output)

if __name__ == "__main__":
    main()