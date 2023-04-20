from Resources.readInput import *
from Resources.intervalsGenerator import *
from quineMcCluskey import *

def main():
    generator = IntervalsGenerator()

    generatedImplicants = generator.generate()

    print("stages:", generator.stages)
    print("implicants: ", ' '.join(map(str, generatedImplicants)))

if __name__ == "__main__":
    main()