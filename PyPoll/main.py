#Import necessary Dependencies
import os
import csv

#Direct to location of data
voter_data = os.path.join("Resources", "election_data.csv")

# Initialize Total Vote Counter
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
candidates = []

#Open data
with open(voter_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#Skip the header
    header = next(csv_reader)
    for row in csv_reader:
#Create unique list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])  
#Create candidate specific vote count
        if row[2] == "Khan":
            khan_votes = khan_votes + 1
        if row[2] == "Correy":
            correy_votes = correy_votes + 1
        if row[2] == "Li":
            li_votes = li_votes + 1
        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1
#Count total number of votes
        total_votes = total_votes + 1

#Calculate candidate percentages
khan_percent = round((100 * (khan_votes / total_votes)),4)
correy_percent = round((100 * (correy_votes / total_votes)),4)
li_percent = round((100 * (li_votes / total_votes)),4)
otooley_percent = round((100 * (otooley_votes / total_votes)),4)

#Create a List of Candidate percentages
vote_percent = [khan_percent, correy_percent, li_percent, otooley_percent]

#Create dictionary of key (candidate) value (percentages) pairs
candidate_percent = dict(zip(candidates, vote_percent))

#specify winner from previous dictionary
winner = max(candidate_percent, key=candidate_percent.get)

#Print Summary Table
print(" ")
print("Election Results")
print("****************************************")
print("Total Votes: " + str(total_votes))
print("****************************************")
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")")
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")")
print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")")
print("****************************************")
print("Winner: " + winner)
print("****************************************")
print(" ")

#Print Election Analysis Table of Findings to .txt file
#Open correct directory for correct file location
os.chdir("Analysis")
#Append printed lines to new .txt file
print("Election Results", file = open("Election Analysis.txt", "a"))
print("****************************************", file = open("Election Analysis.txt", "a"))
print("Total Votes: " + str(total_votes), file = open("Election Analysis.txt", "a"))
print("****************************************", file = open("Election Analysis.txt", "a"))
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")", file = open("Election Analysis.txt", "a"))
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")", file = open("Election Analysis.txt", "a"))
print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")", file = open("Election Analysis.txt", "a"))
print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")", file = open("Election Analysis.txt", "a"))
print("****************************************", file = open("Election Analysis.txt", "a"))
print("Winner: " + winner, file = open("Election Analysis.txt", "a"))
print("****************************************", file = open("Election Analysis.txt", "a"))
#Close .txt file
open("Election Analysis.txt", "a").close()