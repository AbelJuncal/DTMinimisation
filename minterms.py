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
            return Implicant(fusion)
        
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
    entrada = ["001","101","110","111"]
    salida = set()

    while(entrada):
        aux_entrada = list_to_dictionary(entrada)
        listaFusion = []

        print("entrada", aux_entrada, "\n")

        for i in range(0, len(entrada)-1):
            for j in range(i+1, len(entrada)):
                first = [*entrada[i]]
                second = [*entrada[j]]

                diferencia = 0
                fusion = ""

                for z in range(len(first)):
                    if first[z] == second[z]:
                        fusion = fusion + first[z]
                    else:
                        fusion = fusion + "-"
                        diferencia+=1

                print("pareja", first, second)
                
                if(diferencia == 1):
                    listaFusion.append(fusion)
                    aux_entrada[entrada[i]]=1
                    aux_entrada[entrada[j]]=1
                    print("fusion",fusion)

        print("primos", lista_primos(aux_entrada))
        salida.update(lista_primos(aux_entrada))
        
        print("listaFusion", listaFusion)
        print("\n")
        entrada = listaFusion

    print("salida", list(salida))

def list_to_dictionary(list):
    dict = {}

    for element in list:
        dict[element] = 0

    return dict


if __name__ == "__main__":
    stringApproach()