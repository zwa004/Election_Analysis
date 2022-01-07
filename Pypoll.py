# The data we need to retrieve
import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# To do: read and analyze the data here

# Initialize a total vote counter
total_votes = 0

# Initialize variable for list to hold candidates
candidate_options = []

# Declare dictionary for votes for each candidate
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and read election results

with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)

    # Read and print the header row in the CSV file
    headers = next(file_reader)
        
    # Print name of candidates and check total votes with for loop
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate was not on any of the above iterated rows
        if candidate_name not in candidate_options:
        
            # Add candidate name to candidate options list using append
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that cadidate's count
        candidate_votes[candidate_name] += 1
        
    # Save the results to election_analysis
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
        print(election_results)
        # Save the final vote count to the text file
        txt_file.write(election_results)    
        
        
        # Find the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes for that candidate
            vote_percentage = float(votes) / float(total_votes) *100
            # Print the candidate name and percentage of votes
            print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")
        
            # Print out each candidate's name, vote count, and percentage of votes to the terminal
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        
            # Determine the winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If they are then set winning_count = votes and winning_percent = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    # print(winning_candidate_summary)

       
# Print current data summary
# print(total_votes)
#print(candidate_options)        
#print(candidate_votes)




# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# 4 The total number of votes each cadidate won
# 5 The winner of the election based on popular vote