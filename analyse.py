import csv




file = open("sensor_logics.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
sensors_logics = []
for row in csvreader:
    sensors_logics.append(row)
sensors_logics = [x for sublist in sensors_logics for x in sublist]
file.close()

file = open("11_22_30.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
rows = [x for sublist in rows for x in sublist]
print(rows)

differences = list(set(rows) - set(sensors_logics))
print(differences)
file.close()

