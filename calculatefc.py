from Resources.readInput import *
from Resources.intervalsGenerator import *
from quineMcCluskey import *
import sys

def main():

    readInput = ReadInput()

    input = readInput.readIntervalInput('GeneratedExamples/' + sys.argv[1]) 

    newImplicants = set()

    for element in input:
        newImplicants.update(element.unfold(readInput.stages))

    MFC = 1

    for variableStage in readInput.stages:
        MFC = MFC * (len(variableStage)-1)
         
    
    print(readInput.stages)
    print("MFC number is ", MFC)
    print("FC number is ", len(newImplicants))
    print("Covered lines ", (len(newImplicants)/MFC)*100, "%")


if __name__ == "__main__":
    main()