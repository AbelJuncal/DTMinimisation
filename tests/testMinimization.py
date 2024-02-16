from mindt_Selino.dtMinimisation import DtMinimisation

minimization = DtMinimisation("tests/test2/GeneratedExamples/ex.5_3_10")

minimization.printInput()

minimization.printStaggeredInput()

minimization.printOutput()

minimization.saveOutputInFile("output.txt")