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

    #MFC = 1

    #for variableStage in readInput.stages:
    #    MFC = MFC * (len(variableStage)-1)
         
    
    #print(readInput.stages)
    #print("MFC number is ", MFC)
    #print("FC number is ", len(newImplicants))
    #print("Covered lines ", (len(newImplicants)/MFC)*100, "%")

    output = QuineMcCluskey.execute(list(newImplicants))
    
    filename = sys.argv[1]

    with open('PyOutput/' + filename, 'w') as f:
        for implicant in list(output):
            for tuple in implicant.list:
                    for number in tuple:
                        f.write(str(number) + " ")
            f.write("\n")


if __name__ == "__main__":
    main()