from mindt_Selino.Resources.readInput import *
from mindt_Selino.Resources.intervalsGenerator import *
from mindt_Selino.quineMcCluskey import *
import sys

#Recibimos un archivo input
#Lo leemos y tenemos nuestra representación en intervalos
#Ejecutamos el algoritmo
#Devolvemos la salida, se puede guardar en un archivo

class DtMinimisation():
    def __init__(self, path):
        readInput = ReadInput()

        input = readInput.readIntervalInput(path)

        newImplicants = set()

        for element in input:
            newImplicants.update(element.unfold(readInput.stages))

        staggeredImplicants = list(newImplicants)

        output = QuineMcCluskey.execute(staggeredImplicants)

        self.input = input
        self.staggeredImplicants = staggeredImplicants
        self.output = list(output)

    def printInput(self):
        print("Input implicants for the minimizer:\n")
        for implicant in self.input:
            print(implicant)
        print("\n")

    def printStaggeredInput(self):
        print("Staggered implicants from the input:\n")
        for implicant in self.staggeredImplicants:
            print(implicant)
        print("\n")

    def printOutput(self):
        print("Ouput implicants:\n")
        for implicant in self.output:
            print(implicant)
        print("\n")

    def getOutput(self):
        return self.output

    def saveOutputInFile(self, path):
        print("Saving output in " + path)

        with open(path, 'w') as f:
            for implicant in self.output:
                for tuple in implicant.list:
                        for number in tuple:
                            f.write(str(number) + " ")
                f.write("\n")

