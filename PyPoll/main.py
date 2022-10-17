#importing libraries
from itertools import count
import os
import csv
from numpy import round

#set path for file
pypollcsvpath = os.path.join("resources", "election_data.csv")

#open csv file for reading
file =  open(pypollcsvpath, 'r')

#read csv file
csvreader = csv.reader(file, delimiter=",")

#add header
csv_header = next(csvreader)
#print(f"csv header: {csv_header}")

votes = []
candidatesfull = []
candidatesunique = []

#visualize data and make list of votes
for row in csvreader:
    #print(row)
    votes.append(row[0])
    candidatesfull.append(row[2])

#The total number of votes cast
print(f'Election results')
print(f'________________________________________')
print(f'Total votes = {len(votes)}')
print(f'________________________________________')


#A complete list of candidates who received votes
#make list of candidates
for i in candidatesfull:
    if i not in candidatesunique:
        candidatesunique.append(i)
#test candidates list
#for i in candidatesunique:
#    print(f'{i}')
#print(candidatesunique)

#The percentage of votes each candidate won
#votecharles = ((candidatesfull) == "Charles Casper Stockham")
#print(votecharles)
candidatevotes = [0, 0, 0]
for i in candidatesfull:
    for j in range(len(candidatesunique)):
        if i == candidatesunique[j]:
            candidatevotes[j] += 1
#test candidates votes list
#print(candidatevotes)


#The total number of votes each candidate won
#def votesperc (x):
#    print((candidatesunique[x]): (int(candidatevotes[x])) // int(len(votes)) * 100)
print(f'{candidatesunique[0]}: {round(int(candidatevotes[0]) / int(len(votes)) * 100, 3)}% ({int(candidatevotes[0])})')
print(f'{candidatesunique[1]}: {round(int(candidatevotes[1]) / int(len(votes)) * 100, 3)}% ({int(candidatevotes[1])})')
print(f'{candidatesunique[2]}: {round(int(candidatevotes[2]) / int(len(votes)) * 100, 3)}% ({int(candidatevotes[2])})')

#The winner of the election based on popular vote
winnercandidateind = candidatevotes.index(max(candidatevotes))
winnercandidate = candidatesunique[winnercandidateind]
print(f'Winner: {winnercandidate}')


file.close()