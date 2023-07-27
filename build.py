import sys
import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import copy


def main():

    prologTimes = {}

    if(len(sys.argv) < 2):
        print("Please give a test folder")
        return
    
    files = os.listdir('tests/'+sys.argv[1]+'/GeneratedExamples')

    prologTimes = {}

    for file in files:
        splitted = file.split('.')
        prologTimes.update({splitted[1]: []})

    pythonTimes = copy.deepcopy(prologTimes)
    optimizationTimes = copy.deepcopy(prologTimes)

    with open("tests/"+sys.argv[1]+"/times/prologTimes.txt") as f:
       prolog = f.read().splitlines() 

    with open("tests/"+sys.argv[1]+"/times/pythonTimes.txt") as f:
        python = f.read().splitlines()

    with open("tests/"+sys.argv[1]+"/times/optimizedTimes.txt") as f:
        optimized = f.read().splitlines()

    with open("tests/"+sys.argv[1]+"/times/fc.txt") as f:
        calculatefc = f.read().splitlines()

    values = dict()

    for l in calculatefc:
        splitted = l.split(",")
        example = splitted[0].split('.')[1]
        fc = splitted[1]
        mfc = splitted[2]
        values[example] = [fc, mfc]

    for l in prolog:
        splitted = l.split(".")
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[1], minutes, seconds, time)
        else:
            time = 120
            
        prologTimes[splitted[1]].append(time)

    for l in python:
        splitted = l.split(".")
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[1], minutes, seconds, time)
        else:
            time = 120

        pythonTimes[splitted[1]].append(time)

    for l in optimized:
        splitted = l.split(".")
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[1], minutes, seconds, time)
        else:
            time = 120

        optimizationTimes[splitted[1]].append(time)

    print("prolog", prologTimes['7_5_20'])
    print("python", pythonTimes['7_5_20'])
    print("optimized", optimizationTimes['7_5_20'])

    prologList = list(prologTimes.items())
    pythonList = list(pythonTimes.items())
    optimizationList = list(optimizationTimes.items())

    with open("tests/"+sys.argv[1]+"/times/tiempos.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ejecución", "programa", "fc", "mfc", "ejemplo", "tiempo"])
        for t in prologList:
            for i in range(0, 5):
                writer.writerow([i+1, "prolog", values.get(t[0])[0], values.get(t[0])[1], t[0], t[1][i]])

        for p in pythonList:
            for i in range(0,5):
                writer.writerow([i+1, "python", values.get(p[0])[0], values.get(p[0])[1], p[0], p[1][i]])

        for o in optimizationList:
            for i in range(0,5):
                writer.writerow([i+1, "optimized", values.get(o[0])[0], values.get(o[0])[1], o[0], o[1][i]])

    file.close()

    # df = pd.read_csv('tests/'+sys.argv[1]+'/times/tiempos.csv')
    # filtered = df.filter(items = ['programa'])

    # ex = sns.load_dataset("penguins")
    # sns.pairplot(ex, hue="species")

    # plt.show()


if __name__ == "__main__":
    main()