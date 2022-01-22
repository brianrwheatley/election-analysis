# Total number of votes cast
# Complete list of candidates who received votes
# Percentage of votes per candidate
# Vote total per candidates
# Winner of the election based on popular vote
import csv
import os


file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
