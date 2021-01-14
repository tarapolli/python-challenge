import os
import csv

election_csv = os.path.join('resources', 'election_data.csv')

# create lists for holding data
total_votes = []
candiate_name = []
total_candidate = []

# create variables
total_votes = 0

# open and read csv
with open(election_csv) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")

    # skip header row
    next(election_data)

    # begin loop to calculate total votes included in dataset
    for row in election_data:
        total_votes
        total_votes = total_votes + 1
 

        # list of candidates who received votes
        for row in election_data:
            total_votes = total_votes +1


        # percentage of votes each candidate won
        

        # total number of votes each candidate won
            #count_votes = len(candiate_name)

        


# winner of the election based on popular vote
