# Total number of votes cast
# Complete list of candidates who received votes
# Percentage of votes per candidate
# Vote total per candidates
# Winner of the election based on popular vote
import csv
import os


file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialze all the things
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
        #add candidate if not in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #reset total vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    #print(f"{candidate_name} received {vote_percentage:,.1f}% of the vote.")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


