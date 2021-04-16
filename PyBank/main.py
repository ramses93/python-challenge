import csv

def generateAnalysis(data):
    resultsString = ""

    resultsString += 'Financial Analysis\n'
    resultsString += '----------------------------\n'
    resultsString += f'Total Months: {str(data["totalMonths"])}\n'
    resultsString += f'Total: ${str(data["totalChange"])}\n'
    resultsString += f'Average  Change: ${data["averageChange"]}\n'
    resultsString += f'Greatest Increase in Profits: {data["greatestIncrease"]["date"]} (${str(data["greatestIncrease"]["amount"])})\n'
    resultsString += f'Greatest Decrease in Profits: {data["greatestDecrease"]["date"]} (${str(data["greatestDecrease"]["amount"])})\n'

    return resultsString

if __name__ == "__main__":
    analysis = {
        "totalMonths": 0,
        "totalChange": 0,
        "averageChange": "", # Store as string since we need to format accordingly
        "greatestIncrease": {
            "date": "",
            "amount": 0
        },
        "greatestDecrease": {
            "date": "",
            "amount": 0
        }
    }

    with open('Resources/budget_data.csv') as budgetFile:
        csvReader = csv.reader(budgetFile, delimiter= ',')

        # Skipping header row
        next(csvReader)

        for row in csvReader:
            analysis["totalMonths"] += 1
            analysis["totalChange"] += int(row[1])
            if int(row[1]) > analysis["greatestIncrease"]["amount"]:
                analysis["greatestIncrease"]["date"] = row[0]
                analysis["greatestIncrease"]["amount"] = int(row[1])

            if int(row[1]) < analysis["greatestDecrease"]["amount"]:
                analysis["greatestDecrease"]["date"] = row[0]
                analysis["greatestDecrease"]["amount"] = int(row[1])

    analysis["averageChange"] = '{:.2f}'.format(round(analysis["totalChange"] / analysis["totalMonths"], 2))

    outputString = generateAnalysis(analysis)

    with open('analysis/output.txt', 'w') as outputFile:
        outputFile.write(outputString)

    print(outputString)
