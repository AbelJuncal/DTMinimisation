# import sys
# import os
# import csv
# import pandas as pd

# with open("prologTimes.txt") as f:
#     prolog = f.read().splitlines() 

# with open("pythonTimes.txt") as f:
#     python = f.read().splitlines() 

# times = dict()

# for l in prolog:
#     splitted = l.split(".")
#     seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
#     if times.get(splitted[1]) is None:
#         times.update({splitted[1]: [seconds]})
#     else:
#         times[splitted[1]].append(seconds)

# for l in python:
#     splitted = l.split(".")
#     seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
#     times[splitted[1]].append(seconds)

# tiempos = list(times.items())

# with open('tiempos.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["ejecución", "programa", "ejemplo", "tiempo"])
#     for t in tiempos:
#         for i in range(0, 5):
#             writer.writerow([i+1, "prolog", t[0], t[1][i]])
#             writer.writerow([i+1, "python", t[0], t[1][i+5]])

# file.close()

# df = pd.read_csv('tiempos.csv')
# filtered = df.filter(items = ['programa'])

# print(filtered.to_string())

import sys
import os
import csv
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
        prologTimes.update({splitted[0]: []})

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
        example = splitted[0].split('.')[0]
        fc = splitted[1]
        mfc = splitted[2]
        values[example] = [fc, mfc]

    for l in prolog:
        splitted = l.split(".")
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[0], minutes, seconds, time)
        else:
            time = 120
            
        prologTimes[splitted[0]].append(time)

    for l in python:
        splitted = l.split(".")
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[0], minutes, seconds, time)
        else:
            time = 120

        pythonTimes[splitted[0]].append(time)

    for l in optimized:
        splitted = l.split(".")
        print(splitted)
        if splitted[2]!= '':
            minutes = splitted[2].split("m")[0]
            seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
            time = (int(minutes) * 60) + float(seconds)
            print(splitted[0], minutes, seconds, time)
        else:
            time = 120

        optimizationTimes[splitted[0]].append(time)

    prologList = list(prologTimes.items())
    pythonList = list(pythonTimes.items())
    optimizationList = list(optimizationTimes.items())

    with open("tests/"+sys.argv[1]+"/times/tiempos.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["programa", "fc", "mfc", "ejemplo", "tiempo"])
        for t in prologList:
            if len(t[1]) != 0:
                writer.writerow(["prolog", values.get(t[0])[0], values.get(t[0])[1], t[0], t[1][0]])

        for p in pythonList:
            if len(t[1]) != 0:
                writer.writerow(["python", values.get(p[0])[0], values.get(p[0])[1], p[0], p[1][0]])

        for o in optimizationList:
            if len(t[1]) != 0:
                writer.writerow(["optimized", values.get(o[0])[0], values.get(o[0])[1], o[0], o[1][0]])

    file.close()


if __name__ == "__main__":
    main()