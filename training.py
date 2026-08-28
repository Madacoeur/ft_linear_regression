
import csv

mileages = []
prices = []

with open("data.csv", 'r') as file:
    csvreader = csv.reader(file)

    next(csvreader)
    for row in csvreader:
        mileages.append(float(row[0]) /100000)
        prices.append(float(row[1]))
theta0 = float(0)
theta1 = 0.0
learningRate = 0.05
iterations = 1000
def estimatePrice(mileage):
    Eprice = theta0 + (theta1 * mileage)
    return (Eprice)
for i in range(iterations):
    somme_errs_t0 = 0
    somme_errs_t1 = 0
    for j in range (len(mileages)):
        EstPrice = estimatePrice(mileages[j])
        somme_errs_t0 += EstPrice - prices[j]
        somme_errs_t1 += (EstPrice- prices[j]) * mileages[j]
    theta0 = theta0 - learningRate * (somme_errs_t0 / len(mileages))
    theta1 = theta1 - learningRate * (somme_errs_t1 / len(mileages))
with open("thetas.csv", 'w') as fichier:
    fichier.write(str(theta0) + "," + str(theta1))


#print(theta0)
#print(theta1)
#for i in mileages:
 #   print (i)
 #  print('\n')
 #  for i in prices:
 #      print (i)
