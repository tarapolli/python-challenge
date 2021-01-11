import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print (csvreader)
    
 # initialze variables


      
# The total number of months included in the dataset
for row in csvreader
    

# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

