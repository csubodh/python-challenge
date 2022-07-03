"""
This program will loop through all csv data and 
create summary table like 
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)

"""
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# Pull csv file in the program
csvpath = os.path.join('..', 'PyBank/Resources', 'budget_data.csv')
# Create output file to store output
outputfile = os.path.join('..', 'PyBank/analysis', 'PyBankOutput.txt')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Delare summary values
    numberOfMonths = 0
    totalBudget = 0

    # Delclare variables for greatest increase and decrease value and month
    currentMonthChange = 0
    previousMonthBudget = 0

    greatestIncreaseValue= 0 
    previousGreatestIncreaseValue= 0 
    currentGreatestIncreaseValue =0 
    greatestIncreaseValueMonth = ""

    greatestDecreaseValue = 0
    previousGreatestDecreaseValue= 0 
    currentGreatestDecreaseValue =0 
    greatestDecreaseValueMonth = ""

    # Declare variables for average change calculations
    sumOfChange = 0
    numberOfChanges = 0

    # Read each row of data after the header
    for row in csvreader:
        numberOfMonths += 1
        totalBudget = totalBudget + int(row[1])
        currentMonthBudget = int(row[1])
        currentMonth = row[0]

        # Calculate current month change compared to previous month
        # Start calculating change from second row after header (first data row should be ignored for difference)
        if (numberOfMonths > 1):
          currentMonthChange = currentMonthBudget - previousMonthBudget
          sumOfChange = sumOfChange + currentMonthChange
          numberOfChanges += 1

        # Set current greatest increase as months difference  when difference is positive 
        if (currentMonthChange > 0):
          currentGreatestIncreaseValue = currentMonthChange      

        if (currentMonthChange > 0 and (currentGreatestIncreaseValue > previousGreatestIncreaseValue)):
          greatestIncreaseValue = currentGreatestIncreaseValue
          greatestIncreaseValueMonth = currentMonth
          #reset value for previous highest
          previousGreatestIncreaseValue = currentGreatestIncreaseValue
        
        if (currentMonthChange < 0):
          currentGreatestDecreaseValue = currentMonthChange      

        if (currentMonthChange < 0 and (currentGreatestDecreaseValue < previousGreatestDecreaseValue)):
          greatestDecreaseValue = currentGreatestDecreaseValue
          greatestDecreaseValueMonth = currentMonth
          #reset value for previous lowest
          previousGreatestDecreaseValue = currentGreatestDecreaseValue

        #reset values
        previousMonthBudget = currentMonthBudget    

    output = (
      f"\nBank Output\n"
      f"--------------------------------------------------------------"
      f"\nTotal months: {numberOfMonths}"  
      f"\nTotal Budget: {totalBudget}"
      f"\nAverage Change: ${sumOfChange/numberOfChanges}"
      f"\nGreatest Increase month and $: ${greatestIncreaseValueMonth} : {greatestIncreaseValue}"
      f"\nGreatest Decrease month and $: ${greatestDecreaseValueMonth} : {greatestDecreaseValue}"
      f"\n--------------------------------------------------------------\n"
    )

    print(output)

    with open(outputfile, "w") as textfile:
      textfile.write(output)
  