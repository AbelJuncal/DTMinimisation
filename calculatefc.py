from Resources.readInput import *
from Resources.intervalsGenerator import *
from quineMcCluskey import *
import sys

def main():
    if(len(sys.argv) < 3):
        print("Please give a testFolder")
        return

    readInput = ReadInput()

    input = readInput.readIntervalInput('tests/'+sys.argv[1]+'/GeneratedExamples/' + sys.argv[2]) 

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