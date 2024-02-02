from mindt_Selino.Resources.readInput import *
from mindt_Selino.Resources.intervalsGenerator import *
from mindt_Selino.optimizedQuineMcCluskey import *
import sys

def main():

    readInput = ReadInput()

    input = readInput.readOptimizedIntervalInput('tests/'+sys.argv[1]+'/GeneratedExamples/' + sys.argv[2]) 

    newImplicants = set()

    for element in input:
        newImplicants.update(element.unfold(readInput.stages))

    output = OptimizedQuineMcCluskey.execute(list(newImplicants), readInput.stages)
    
    filename = sys.argv[2]

    with open('tests/'+sys.argv[1]+'/optimizedOutput/' + filename, 'w') as f:
        for implicant in list(output):
            for tuple in implicant.list:
                    for number in tuple:
                        f.write(str(number) + " ")
            f.write("\n")


if __name__ == "__main__":
    main()