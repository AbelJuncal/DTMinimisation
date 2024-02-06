from mindt_Selino.dtMinOptimized import DtMinOptimized

minimization = DtMinOptimized("tests/test2/GeneratedExamples/ex.5_3_10")

minimization.printInput()

minimization.printStaggeredInput()

minimization.printOutput()

minimization.saveOutputInFile("output.txt")