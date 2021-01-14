import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # skip header row
    next(csv_reader)

# create lists to store data
total_months = []   # store the count of number rows from column 1 []
total_profit = []   # store all of profit/losses from column 2 []]
month_diff = []     # difference b/t each month
month__diff_add = []   # store all months in difference b/t current and previous rows

#total_months = 0
#total_profit = 0
count = 0


# begin loop on first row
for row in csv_reader:
   if count == 0:
       # keep adding 1 to count rows  # profit_loss = profit_loss + row[1]
        count = count + 1
        # store this new value in list
        new_count = int(row[1])  ###
        # append variable counters
        total_months.append = int(row[0])
        total_profit.append = int(row[1])
    # contiue loop thru remainder rows
    else:
        # adds to lists
        total_months.append = int(row[0])
        total_profit.append = int(row[1])
        # calculate difference between current row & previous row
        month_diff.append(int(int(row[1])  - new_count))
        # add to difference in months
        month__diff_add.append(int(row[0]))
        # revised list containing all month changes
        new_count = int(row[1])

    # calculate results for summary table
    # total months
    TotalMonths = sum(months)

    # total profit
    TotalProfit = sum(total_profit)
    # average change
    Average = (month__diff_add/new_amount)
    # maximum change
    MaxProfit = max(total_profit)
    # minimum change
    MinProfit = min(total_profit)
    
