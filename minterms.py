
def lista_primos(dicImplicantes):
    listaPrimos = []
    for x , y in dicImplicantes.items():
        if y == 0:
            listaPrimos.append(x)

    return listaPrimos

def stringApproach():
    #entrada = [("001", 0),("101", 0),("110", 0),("111", 0)]
    salida = set()

    # while(entrada):
    #     print("\nNueva iteracion\n")
    #     aux_entrada = dict(entrada)
    #     listaFusion = {}

    #     print("entrada", aux_entrada, "\n")

        #TODO como miro si se pueden relacionar más, mirar si es primo, guardar de que implicantes salen
        # for i in range(0, len(entrada)-1):
        #     for j in range(i+1, len(entrada)):
        #         first = [*entrada[i][0]]
        #         second = [*entrada[j][0]]

        #         diferencia = 0
        #         fusion = ""

        #         for z in range(len(first)):
        #             if first[z] == second[z]:
        #                 fusion = fusion + first[z]
        #             else:
        #                 fusion = fusion + "-"
        #                 diferencia+=1

        #         print("pareja", first, second)
                
        #         if(diferencia == 1):
        #             listaFusion[fusion]=0
        #             aux_entrada[entrada[i][0]]=1
        #             aux_entrada[entrada[j][0]]=1
        #             print("fusion",fusion)

        # print("primos", lista_primos(aux_entrada))
        # salida.update(dict(lista_primos(aux_entrada)))
        
        # print("listaFusion", listaFusion)
        # print("\n")
        # entrada = list(listaFusion.items())

    entrada = ["001","101","110","111"]

    while(entrada):
        aux_entrada = list_to_dictionary(entrada)
        listaFusion = []

        print("entrada", aux_entrada, "\n")

        #TODO como miro si se pueden relacionar más, mirar si es primo, guardar de que implicantes salen
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