import csv

kilometrage = float(input("Quel est le kilometrage de la voiture?")) / 100000

try:
    with open("thetas.csv", 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            theta0 = float(row[0])
            theta1 = float(row[1])
except FileNotFoundError:
    theta0 = 0
    theta1 = 0
EstimatedPrice = theta0 + (theta1 * kilometrage)
print(EstimatedPrice)
