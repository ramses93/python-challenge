import numpy as np
import csv


def printAnalysis(candidates, totalVotes):
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-------------------------")

    for key, value in candidates.items():
        print(key + ": " + '{:.3f}'.format(round(value / totalVotes*100, 3)) + "% (" + str(value) + ")")

    print("-------------------------")
    print("Winner: ")
    print("-------------------------")

if __name__ == "__main__":
    candidates = {}
    
    i = 0

    with open('Resources/election_data.csv') as electionPollFile:
        csvReader = csv.reader(electionPollFile, delimiter= ',')

        # Skipping header row
        next(csvReader)

        for row in csvReader:
            i = i+1
            if row[2] in candidates:
                candidates[row[2]] = candidates[row[2]] + 1
            else:
                candidates[row[2]] = 1

    print(candidates)
    print(i)

    printAnalysis(candidates, i)


