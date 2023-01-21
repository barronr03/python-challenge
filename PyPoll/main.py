import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")
# Open the CSV file and read the contents
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 
    #Set the variable and create a dictionary to store vote count for each candidate
    total_votes = 0
    candidate_votes = {} 
    candidates = set()

    # count votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        candidates.add(candidate)
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")

# print vote count and percentage for each candidate
for candidate in candidates:
    vote_count = candidate_votes.get(candidate, 0)
    vote_percentage = round((vote_count / total_votes) * 100, 3)
    print(f'{candidate}: {vote_percentage}% ({vote_count})')

print("----------------------------")

# determine the winner of the election
winner = max(candidate_votes, key=candidate_votes.get)
print(f'Winner: {winner}')

# Create text file with the results
with open("resultsPyPoll.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write('-------------------------------\n')
    text_file.write(f'Total Votes:  {total_votes}\n')
    text_file.write('-------------------------------\n')
    for candidate in candidates:
        vote_count = candidate_votes.get(candidate, 0)
        vote_percentage = round((vote_count / total_votes) * 100, 3)
        text_file.write(f'{candidate}: {vote_percentage}% ({vote_count})\n')
    text_file.write('-------------------------------\n')
    text_file.write(f'Winner: {winner}')
