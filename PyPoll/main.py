#import modules
import os
import csv

#set local pc path to data csv file
csvpath = os.path.join("resources", "election_data.csv")

#create votes dictionary
candidates_list = {}
counter = 0

# open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header row
    next(csv_reader, None)

    # begin loop
    for row in csv_reader:
        #define candidate column
        candidate = row[2]

        #if candidate not in dictionary, add with first vote
        if candidate not in candidates_list:
            candidates_list[candidate] = 1

        #if candidate already in dictionary, add a vote
        else:
            candidates_list[candidate] += 1

#for key, value in votes.items():
    #print(f'{key} : {value}')

# add values in dictionary to get total votes
votes = candidates_list.values()
Total_Votes = sum(votes)

# use max function to identify winning candidate
# def get_max(Total_Votes):
#     votemax = 0
#     for votemax in candidate:
#         if votemax < candidates_list
#     return votemax
#     maxcandidate = get_max(candidates)
    #print(maxcandidate)

# print summary table
print(f'Election Results')
print(f'Total Votes: {Total_Votes}')
#for key, value in candidates_list.items():
#    print(f'{candidate}: {votes / Total_Votes: 3%} ({Total_Votes})")


# write summary table to output file
# specify file to write to
output_path = os.path.join("analysis", "PyPoll_Summary.txt")