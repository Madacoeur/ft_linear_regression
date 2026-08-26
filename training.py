
import csv

mileages = []
prices = []

with open("data.csv", 'r') as file:
    csvreader = csv.reader(file)

    next(csvreader)
    for row in csvreader:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))
    for i in mileages:
        print (i)
    for i in prices:
        print (i)

