# minDt
A ferramenta de código aberto que permite mellorar a explicabilidade das saídas das árbores de decisión. Está basada no algoritmo de Quine-McCluskey, representando os camiños dunha árbore de decisión como implicantes de intervalos de valores.

## Estrutura do repositorio

> - `/src`: aquí atópase o código fonte da ferramenta. Atopamonos con dúas implementacións, onde a segunda representa unha optimización da primeira.
> - `/tests`: aquí atópanse exemplos de árbores reais e sintéticos que se usaron durante o desenvolvemento para probar o funcionamento do código. Tamén se inclúen unha implementación do algoritmo en prolog e diversos scripts de bash para comparar os tempos de execución das implementacións. Tamén hai algúns scripts usados para xerar .csv cos tempos e a construcción e gráficas.

## Instalación

O paquete atópase dispoñible en Pypi polo que, para a súa instalación, sería suficiente con executar o siguiente comando.

```bash
pip install mindt-Selino
```

Para o uso do código en si, é suficiente con ter instalado Python >3.8. Se se quere indagar nas probas de tempos e demais, hai máis dependencias que se deberían instalar como seaborn, numpy ou pandas.

## Formato de entrada

A entrada da ferramenta para poder minimizar unha árbore ten que respetar o seguinte formato: 

```bash
3
100
100
100
50 100 0 50 50 100 
0 100 50 100 50 100 
50 100 50 100 0 50 
50 100 0 100 50 100 
50 100 50 100 50 100 
```

Onde a primeira liña representa o número de variables. As n seguintes o valor máximo da variable (supoñendo que o valor mínimo é cero) e as restantes todos as regras que clasifican nunha mesma instancia. Pódese tamén pasar un valor mínimo para cada variable. O funcionamento está pensado para árbores binarias, polo cal, os implicantes poderían representar unha clase ou a outra pero non as dúas. Cada un dos implicantes ven dado por parellas de valores que representan os intervalos de cada variable nesa solución. Se a variable non aparece nesa regra, o intervalo vai ser o valor mínimo e máximo da variable.



## Exemplos de uso

Neste apartado inclúense dous pequenos scripts de exemplo para poder probar a ferramenta. Este código pódese atopar na carpeta tests nos ficheiros **testMinimization.py** e **testOptimized.py**.

```python
from mindt_Selino.dtMinimisation import DtMinimisation

minimization = DtMinimisation("tests/test2/GeneratedExamples/ex.5_3_10")

minimization.printInput()
minimization.printStaggeredInput()
minimization.printOutput()

minimization.saveOutputInFile("output.txt")
```
Neste primeiro caso estamos minimizando un dos exemplos sintéticos, onde o ficheiro está no formato de entrada especificado e facemos uso das función da clase **DtMinimization** para ir imprimindo o conxunto de regras según van pasando fases da execución. Tamén se pode usar a saída, representada como unha lista de implicantes. Finalmente gardase a saída no path que se lle pasa como parámetro. 

Con só crear unha instancia, o proceso de minimización xa comeza automaticamente.

```python
from mindt_Selino.dtMinOptimized import DtMinOptimized

minimization = DtMinOptimized("tests/test2/GeneratedExamples/ex.5_3_10")

minimization.printInput()
minimization.printStaggeredInput()
minimization.printOutput()

minimization.saveOutputInFile("output.txt")
```

O mesmo pero para un intento de optimización do código que non funcionou como se esperaba.


## Licenza

Este proxecto atópase baixo a licenza de código aberto Mozilla. Véxase [LICENSE](https://github.com/AbelJuncal/DTMinimisation/blob/main/LICENSE).
