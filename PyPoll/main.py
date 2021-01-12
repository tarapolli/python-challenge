import os
import csv

election_csv = os.path.join('resources', 'election_data.csv')

# intialize variables
total_votes = []
candiate_name = []
voter_id = []


# open and read csv
with open(election_csv) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")


    # skip header row
    next(election_data)

# loop thru ____


# The total number of votes cast (row count or voter IDs)
#for row in election_csv
 #   voter_id.append(2)


# list of candidates who received votes

# percentage of votes each candidate won

# total number of votes each candidate won
#total_votes = 
for vote in election_csv:
    if candiate_name == "Khan"

    count_votes = len(candiate_name)




# winner of the election based on popular vote
