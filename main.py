from Resources.readInput import *
from Resources.intervalsGenerator import *
from quineMcCluskey import *
import sys

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput("GeneratedExamples/" + sys.argv[1])
    
    output = QuineMcCluskey.execute(input)
    
    Resources.printOutput(input, output)

    filename = sys.argv[1]

    print(filename)

    with open('PyOutput/' + filename, 'w') as f:
        for implicant in list(output):
            for tuple in implicant.list:
                    for number in tuple:
                        f.write(str(number) + " ")
            f.write("\n")


if __name__ == "__main__":
    main()