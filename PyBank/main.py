import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    

# skip header row

 # initialze variables
months = []
profit = []   # list to store all of profit/losses from column 2



# The total number of months included in the dataset
for months in csv_reader:
    if row ????
        months.append(row[0])
print(months)

    #or

myList = csv_reader[0]
months.append[0]
print(months)

# The net total amount of "Profit/Losses" over the entire period
#for row in csv_reader:
 

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #def mean(sample):
    #    return sum(sample) / len(sample)

    #mean([1, 2, 3, 4])

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

