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
        #track vote count
        candidate_votes[candidate_name] += 1

#save to text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Vote Totals: {total_votes:,}\n"
        f"-----------------------\n\n"
    )
    print(election_results,end="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        #set votes and calculate percentages
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #iterate and replace to find vote winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

    winning_candidate_summary = (
            f"\n-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
