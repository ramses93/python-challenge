import csv

def generateAnalysis(candidates, totalVotes):
    winningCandidate = ''
    winningNumberofVotes = 0
    
    resultsString = ''

    resultsString += 'Election Results\n'
    resultsString += '-------------------------\n'
    resultsString += f'Total Votes: {str(totalVotes)}\n'
    resultsString += '-------------------------\n'

    for key, value in candidates.items():
        if value > winningNumberofVotes:
            winningNumberofVotes = value
            winningCandidate = key
        resultsString += f'{key}: {"{:.3f}".format(round(value / totalVotes*100, 3))}% ({str(value)})\n'

    resultsString += '-------------------------\n'
    resultsString += f'Winner: {winningCandidate}\n'
    resultsString += '-------------------------\n'

    return resultsString

if __name__ == "__main__":
    candidates = {}
    
    i = 0

    with open('Resources/election_data.csv') as electionPollFile:
        csvReader = csv.reader(electionPollFile, delimiter= ',')

        # Skipping header row
        next(csvReader)

        for row in csvReader:
            i += 1
            if row[2] in candidates:
                candidates[row[2]] += 1
            else:
                candidates[row[2]] = 1

    outputString = generateAnalysis(candidates, i)

    with open('analysis/output.txt', 'w') as outputFile:
        outputFile.write(outputString)

    print(outputString)


