
import csv

mileages = []
prices = []

with open("data.csv", 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        if i == 0:
            mileages.append(float(row[i]))
        else:
            prices.append(float(row[i]))
    for i in mileages:
        print (mileages[i])
