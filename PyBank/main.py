import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# create lists to store data
total_months = []   # store the count of number rows from column 1 []
total_profit = []   # store all of profit/losses from column 2 []]
month_diff = []     # difference b/t each month
month__diff_add = []   # store all months in difference b/t current and previous rows

# create counters
count = 0
max_increase_month = ''
max_decrease_month = ''
max_increase = 0
max_decrease = 9999999

# open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # skip header row
    next(csv_reader, None)

    # begin loop on first row
    for row in csv_reader:

        if count == 0:
            # keep adding 1 to count rows  # profit_loss = profit_loss + row[1]
            count = count + 1
            # store this new value in list
            new_profit_loss = int(row[1]) 
            # append variable counters
            total_months.append(str(row[0]))
            total_profit.append(int(row[1]))
        else:
            # adds to lists
            total_months.append(str(row[0]))
            total_profit.append(int(row[1]))
            # calculate difference between current row & previous row
            month_diff.append(int(int(row[1])  - new_profit_loss))
            # add to difference in months
            month__diff_add.append(str(row[0]))
            diff = int(row[1])  - new_profit_loss
            if diff > max_increase:
                max_increase = diff
                max_increase_month = row[0]
            if diff < max_decrease:
                max_decrease = diff
                max_decrease_month = row[0]
            # revised list containing all month changes
            new_profit_loss = int(row[1])

    # calculate results for summary table
   
    # total months
    TotalMonths = len(total_months)
   
    # total profit
    TotalProfit = sum(total_profit)

    # average change
    def get_ave_change(list):
        all_the_numbers = 0
        number_count=len(list)
        for number in list:
            all_the_numbers = all_the_numbers + number
            average=all_the_numbers/number_count
        return average
    AverageChange = round(get_ave_change(month_diff),2)

    

# print summary table here
print(f"Financial Analysis")
print(f"------------------")
print(f'Total Months: {TotalMonths}')
print(f'Total Profit: $ {TotalProfit}')
print(f'Average Change: {AverageChange}')
print(f'Greatest Increase In Profits: {max_increase_month} ($ {max_increase})')
print(f'Greatest Decrease In Profits: {max_decrease_month} ($ {max_decrease})')


# write summary table to output file
# specify file to write to
output_path = os.path.join("analysis", "PyBank_Summary.txt")
