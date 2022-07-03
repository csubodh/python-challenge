"""
This program will loop through all csv data and 
create summary table like 
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-----------------------
"""
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Pull csv file in the program
csvpath = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')
# Create output file to store output
outputfile = os.path.join('..', 'PyPoll/Resources', 'PyPollOutput.txt')

# Declare variables
totalNumberOfVotes = 0 # Total number votes
listOfCandidates = [] # An array to hold list of candidates
listOfCandidatesVotes = {} # A dictionary that will hold number of votes each candidate received
listofCadidatePercentageOutput = "" # Create output list that contains candidate and % vote
winingCount = 0
winningCandidate = ""

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
        totalNumberOfVotes +=1
        # Add each candidate to array if not in array
        if row[2] not in listOfCandidates:
            listOfCandidates.append(row[2])
            # Build a dictionary of candidate and number of votes, start at 1 for first occurance 
            listOfCandidatesVotes[row[2]] = 1
        else:
            # Add to candidate number of votes count
            listOfCandidatesVotes[row[2]] +=1

    # Loop though dictionary to get % vote share for each candidate
    for candidate in listOfCandidatesVotes:
        candidateVote = listOfCandidatesVotes.get(candidate)
        votePercent = (float(candidateVote)/ float(totalNumberOfVotes))*100
        listofCadidatePercentageOutput += f"Candidate: {candidate}:{votePercent: .3f}% ({candidateVote}) \n"

        # Identify winning candidate
        if candidateVote > winingCount:
            winningCandidate = candidate
            # set winning count as candidate vote
            winingCount = candidateVote
    
output = (
    f"\nPoll Output\n"
    f"--------------------------------------------------------------"
    f"\nTotal Number of votes: {totalNumberOfVotes}\n"  
    f"--------------------------------------------------------------"
    f"\n{listofCadidatePercentageOutput}"  
    f"--------------------------------------------------------------"
    f"\nThe winning candidate is: {winningCandidate}\n"  
    f"--------------------------------------------------------------"
    )

print(output)

with open(outputfile, "w") as textfile:
    textfile.write(output)
  
       
