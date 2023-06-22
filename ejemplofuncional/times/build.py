import sys
import os
import csv
import pandas as pd


def main():

    if(len(sys.argv) < 2):
        print("Please give a test folder:")


    with open("prologTimes.txt") as f:
        prolog = f.read().splitlines() 

    with open("pythonTimes.txt") as f:
        python = f.read().splitlines() 

    times = dict()

    for l in prolog:
        splitted = l.split(".")
        seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
        if times.get(splitted[1]) is None:
            times.update({splitted[1]: [seconds]})
        else:
            times[splitted[1]].append(seconds)

    for l in python:
        splitted = l.split(".")
        seconds = splitted[2].split("m")[1].split("s")[0].replace(",", ".")
        times[splitted[1]].append(seconds)

    tiempos = list(times.items())

    with open('tiempos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ejecución", "programa", "ejemplo", "tiempo"])
        for t in tiempos:
            for i in range(0, 5):
                writer.writerow([i+1, "prolog", t[0], t[1][i]])
                writer.writerow([i+1, "python", t[0], t[1][i+5]])

    file.close()

    df = pd.read_csv('tiempos.csv')
    filtered = df.filter(items = ['programa'])

    print(filtered.to_string())

if __name__ == "__main__":
    main()