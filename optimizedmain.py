from Resources.readInput import *
from Resources.intervalsGenerator import *
from optimizedQuineMcCluskey import *
import sys

def main():

    readInput = ReadInput()

    input = readInput.readOptimizedIntervalInput('tests/test2/GeneratedExamples/' + sys.argv[1]) 

    newImplicants = set()

    for element in input:
        newImplicants.update(element.unfold(readInput.stages))

    output = OptimizedQuineMcCluskey.execute(list(newImplicants), readInput.stages)
    
    filename = sys.argv[1]

    with open('tests/test2/PyOutput/' + filename, 'w') as f:
        for implicant in list(output):
            for tuple in implicant.list:
                    for number in tuple:
                        f.write(str(number) + " ")
            f.write("\n")


if __name__ == "__main__":
    main()