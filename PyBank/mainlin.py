import os
import csv

csvpath = os.path.join('resources', 'budget_data.csv')

# create lists to store data
total_months = []   # store the count of number rows from column 1 []
total_profit = []   # store all of profit/losses from column 2 []]
month_diff = []     # difference b/t each month
month__diff_add = []   # store all months in difference b/t current and previous rows


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
            new_count = int(row[1])  ###
            # append variable counters
            total_months.append(str(row[0]))
            total_profit.append(int(row[1]))
        else:
            # adds to lists
            total_months.append(str(row[0]))
            total_profit.append(int(row[1]))
            # calculate difference between current row & previous row
            month_diff.append(int(int(row[1])  - new_count))
            # add to difference in months
            month__diff_add.append(str(row[0]))
            diff = int(row[1])  - new_count
            if diff > max_increase:
                max_increase = diff
                max_increase_month = row[0]
            if diff < max_decrease:
                max_decrease = diff
                max_decrease_month = row[0]
            # revised list containing all month changes
            new_count = int(row[1])

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

    # maximum change
    def get_max(list):
        countmax = 0
        for number in list:
            if countmax < number:
                countmax = number
        return countmax
    MaxChange = get_max(month_diff)

    # minimum change
    def get_min(list):
        countmin = 0
        for number in list:
            if countmin > number:
                countmin = number
        return countmin
    MinChange = get_min(month_diff)

# print summary table here
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(TotalMonths))
print("Total Profit: $" + str(TotalProfit))
print("Average Change: " + str(AverageChange))
print("Greatest Increase In Profits:" +  " $" + str(MaxChange))
print("Greatest Decrease In Profits:" +  " $" + str(MinChange))

# write summary table to output file
# specify file to write to
output_path = os.path.join("analysis", "PyBank_Summary.csv")

# open file using "write" mode. 
with open(output_path, 'w', newline='') as csvfile:
    # initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')



# maximum change
    #def get_max(list):
        #countmax = 0
        #for number in list:
            #if countmax < number:
                #countmax = number
        #return countmax
    #MaxChange = get_max(month_diff)

    # minimum change
    #def get_min(list):
        #countmin = 0
        #for number in list:
            #if countmin > number:
                #countmin = number
        #return countmin
    #MinChange = get_min(month_diff)