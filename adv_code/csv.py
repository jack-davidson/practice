#!/usr/bin/env python3
from header import Headers

delimeter = ','


def load_csv(file, delimeter=','):
    csv_data = []
    for line in file:
        line = line.strip('\n')
        csv_data.append(line.split(delimeter))
    return csv_data


csv_file = open("file.csv", "r")

csv_data = load_csv(csv_file, delimeter=delimeter)

asian_continents = 0

for i in range(0, len(csv_data)):
    if csv_data[i][Headers.CONTINENT] == "Asia":
        asian_continents += 1

    print(csv_data[i][Headers.CONTINENT], end="\n\t")

print("\nAsian Continents listed in this database: " + str(asian_continents))
csv_file.close()
