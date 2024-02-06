from mindt_Selino.dtMinOptimized import DtMinOptimized
import sys

def main():
    print(sys.argv[0])
    if len(sys.argv)<2:
        print("Please give a file path")
        return

    minimizer = DtMinOptimized(sys.argv[1])
    print("minimized")
    
    if len(sys.argv) > 2:
        minimizer.saveOutputInFile(sys.argv[2])

if __name__ == "__main__":
    main()