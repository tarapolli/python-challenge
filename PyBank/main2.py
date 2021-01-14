import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

  # skip header row
    next(budget_data)

    print (budget_data)
    
# create lists for holding data
date = []
profit = []

#initialize variables
total_months = 0

    # begin loop to calculate total months included in dataset
    for row in csv_reader:
    total_months = total_months + 1

    # calculate net total amt of "Profit/Losses"
    total_profit = total_profit + int(row[0])

      
# The total number of months included in the dataset
# total_months = 0
    for row in budget_data:
        date.append(row[0])
        profit.append(row[1])
        total_months = total_months + 1

print("Total Months:" + str(total_months)) 