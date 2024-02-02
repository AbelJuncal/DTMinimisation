import sys
from mindt_Selino.Resources.intervalsGenerator import *

def main():
    arguments = sys.argv

    steps = [int(i) for i in sys.argv[1].strip('][').split(',')]

    implicants = [int(i) for i in sys.argv[2].strip('][').split(',')]

    vars = [int(i) for i in sys.argv[3].strip('][').split(',')]

    #print(steps, implicants, vars)

    for s in steps:
        for i in implicants:
            for v in vars:
                generator = IntervalsGenerator()
                generatedImplicants = generator.generate(v, s, i)

                filename = "ex." + str(v) + "_" + str(s) + "_" + str(i)

                with open('GeneratedExamples/' + filename, 'w') as f:
                    f.write(str(v) + '\n')

                    for stage in generator.stages:
                        f.write(str(max(stage)) + "\n")

                    for implicant in generatedImplicants:
                        for tuple in implicant.list:
                            for number in tuple:
                                f.write(str(number) + " ")
                        f.write("\n")

                #print("\nSteps: ",s, " Vars: ", v, " Imlicants: ", i, "Filename: ", filename)
                #print("numStages: ", generator.maxStages, "stages:", generator.stages)
                #print("implicants: ", '\n'.join(map(str, generatedImplicants)))



if __name__ == "__main__":
    main()