from mindt_Selino.Implicant.booleanImplicant import *
from mindt_Selino.Implicant.intervalmplicant import *
from mindt_Selino.Implicant.optimizedintervalImplicant import *

class ReadInput():
    @classmethod
    def readBooleanInput(self, filename):
        file = open(filename)
        lines = file.read().splitlines()
        input = []

        for line in lines:
            implicant = BooleanImplicant(line)
            input.append(implicant)

        return input
    
    @classmethod
    def readIntervalInput(self, filename):
        file = open(filename)
        lines = file.read().splitlines()
        input = []
        
        numVariables = int(lines[0])
        lines.pop(0)

        setsList = []

        for i in range(numVariables):
            nuevoSetVariable = set()
            nuevoSetVariable.update([0, int(lines[0])])
            lines.pop(0)
            setsList.append(nuevoSetVariable)

        for element in lines:
            x = element.split()
            tuples = [] 
            nueva_lista = [x[i:i+2] for i in range(0, len(x), 2)]

            for i in range(numVariables):
                lista = nueva_lista[i]
                nuevatupler = []

                for elementer in lista:
                    setsList[i].add(int(elementer))
                    nuevatupler.append(int(elementer))

                nuevatupler = tuple(nuevatupler)
                tuples.append(nuevatupler)

            input.append(IntervalImplicant(tuples))

        for i in range(numVariables):
            setordenado = sorted(setsList[i])
            setsList[i] = setordenado

        self.stages = setsList

        return input
    
    @classmethod
    def readOptimizedIntervalInput(self, filename):
        file = open(filename)
        lines = file.read().splitlines()
        input = []
        
        numVariables = int(lines[0])
        lines.pop(0)

        setsList = []

        for i in range(numVariables):
            nuevoSetVariable = set()
            nuevoSetVariable.update([0, int(lines[0])])
            lines.pop(0)
            setsList.append(nuevoSetVariable)

        for element in lines:
            x = element.split()
            tuples = [] 
            nueva_lista = [x[i:i+2] for i in range(0, len(x), 2)]

            for i in range(numVariables):
                lista = nueva_lista[i]
                nuevatupler = []

                for elementer in lista:
                    setsList[i].add(int(elementer))
                    nuevatupler.append(int(elementer))

                nuevatupler = tuple(nuevatupler)
                tuples.append(nuevatupler)

            input.append(optimizedIntervalImplicant(tuples))

        for i in range(numVariables):
            setordenado = sorted(setsList[i])
            setsList[i] = setordenado

        self.stages = setsList

        return input