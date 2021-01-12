import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print (csvreader)
    
 # initialze variables
date = []
profit = []

      
# The total number of months included in the dataset
for row in csvreader:
    date.append(row[0])
    print(row)