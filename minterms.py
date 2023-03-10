class Implicant():
    def matches(otherImplicant):
        raise "This class is not intended to be instantiated"
    
class BooleanImplicant(Implicant):
    def __init__(self, string):
        self.string = string

    def matches(self, otherImplicant):
    
        diferencia = 0
        fusion = ""

        for z in range(len(self.string)):
            if self.string[z] == otherImplicant.string[z]:
                fusion = fusion + self.string[z]
            else:
                fusion = fusion + "-"
                diferencia+=1

        if(diferencia == 1):
            return BooleanImplicant(fusion)
        
        return None

    def __str__ (self):
        return self.string

def lista_primos(dicImplicantes):
    listaPrimos = []
    for x , y in dicImplicantes.items():
        if y == 0:
            listaPrimos.append(x)

    return listaPrimos

def stringApproach():
    entrada = [BooleanImplicant("001"),BooleanImplicant("101"), BooleanImplicant("110"), BooleanImplicant("111")]
    salida = set()

    print("entrada", ' '.join(map(str, entrada))) 

    while(entrada):
        aux_entrada = list_to_dictionary(entrada)
        listaFusion = []

        for i in range(0, len(entrada)-1):
            for j in range(i+1, len(entrada)):
                first = entrada[i]
                second = entrada[j]

                fusion = first.matches(second)
                
                if fusion:
                    listaFusion.append(fusion)
                    aux_entrada[first]=1
                    aux_entrada[second]=1

        salida.update(lista_primos(aux_entrada))
        
        entrada = listaFusion

    print("salida", ' '.join(map(str, salida)))

def list_to_dictionary(list):
    dict = {}

    for element in list:
        dict[element] = 0

    return dict


if __name__ == "__main__":
    stringApproach()