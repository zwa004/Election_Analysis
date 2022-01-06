# The data we need to retrieve
import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# To do: read and analyze the data here
# Open and read election results

with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)

    # Read and print the header row in the CSV file
    headers = next(file_reader)
    print(headers)
        
        


# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each cadidate won
# 5 The winner of the election based on popular vote