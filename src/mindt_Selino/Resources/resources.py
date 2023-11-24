class Resources(object):
    
    @classmethod
    def primeImplicants(self, dicImplicants):
        primeList = []
        for x , y in dicImplicants.items():
            if y == 0:
                primeList.append(x)

        return primeList

    @classmethod
    def printOutput(self, input, output):
        print("input\n", '\n'.join(map(str, input))) 
        print("output\n", '\n'.join(map(str, output)))

    @classmethod
    def listToDictionary(self, list):
        dict = {}

        for element in list:
            dict[element] = 0

        return dict
