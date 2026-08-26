
import csv

mileages = []
prices = []

with open("data.csv", 'r') as file:
    csvreader = csv.reader(file)

    next(csvreader)
    for row in csvreader:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))
theta0 = float(0)
theta1 = 0.0
learningRate = 0.05
iterations = 1000
def estimatePrice(mileage):
    Eprice = theta0 + (theta1 * mileage)
    return (Eprice)
#for i in mileages:
 #   print (i)
 #  print('\n')
 #  for i in prices:
 #      print (i)
