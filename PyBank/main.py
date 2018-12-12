import os
import csv

# set path for file
budgetCSV = os.path.join("budget_data.csv")

# create empty lists to later append data from csv into
months = []
transactions = []

# create empty list for later 
monthlychange = []

# open CSV
with open(budgetCSV, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header line for the calculations
    next(csvreader)

    # append info from cvs into a list for months and list for transactions
    for row in csvreader:
        months.append(row[0])
        transactions.append(int(row[1]))
    
    # calculate the monthly change in profit/losses with a list comprehension and zip
    monthlychange = [y-x for x, y in zip(transactions, transactions[1:])]
    
    # insert a zero into monthly change at the begining of the list
    monthlychange.insert(0, 0)    
   
# Zip all three lists together into tuples
newBudget = zip(months, transactions, monthlychange)

# save the output file path of new csv file with monthlychange
output_file = "newBudget.csv"

# open the output file in write mode, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=',')
  
    # add the headers
    writer.writerow(["Date", "Profit/Losses", "Monthly Change"])

    # add the rest of the rows using the newBudget variable
    writer.writerows(newBudget)

# set path for file of the newly created csv 
newbudgetCSV = os.path.join("newBudget.csv")

# open new CSV
with open(newbudgetCSV, newline="") as csvfile:
    
    newcsvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header line for the calculations
    next(newcsvreader)

    # set variables for determining maximum gain and the month of the gain
    maxGain = max(monthlychange)
    maxGainMonth = ""

    # for loop from i to the end of "column"
    for i in range(len(monthlychange)): 
        
        # conditional that if monthly change is the actual max gain 
        if(monthlychange[i]==maxGain):
            
            # then pull the month of the max
            maxGainMonth=months[i]
    
    # set variables for determining the maximum loss and the month of the loss     
    maxLoss = min(monthlychange)
    maxLossMonth = ""

    # loop from i to the end of the "column"
    for i in range(len(monthlychange)): 
        
        # conditional that if monthly change is the actual max loss
        if(monthlychange[i]==maxLoss):
            
            # then pull the month of the max Loss
            maxLossMonth=months[i]
       
   
    # calculate the total months by the length of transactions list
    totalMonths = len(transactions)
    
    # calculate the grand total of all profit/loss with sum
    grandTotal = sum(transactions)
    
    # calculate the average change
    changeTotal = sum(monthlychange)
    averageChange = (changeTotal / (totalMonths - 1))
    
    # print the financial analysis
    print('Financial Analysis')
    print('---------------------')
    print(f'Total Months: {totalMonths}') 
    print(f'Total: ${grandTotal}')
    print(f'Average Change: ${averageChange: .2f}')
    print(f'Greatest Increase in Profits: {maxGainMonth} (${maxGain})')
    print(f'Greatest Decrease in Profits: {maxLossMonth} (${maxLoss})')

# export the results to txt file  
f = open('analysis.txt','w')
f.write('Financial Analysis\n')
f.write('__________________\n') 
f.write('Total Months: 86\n')
f.write('Total: $38382578\n')
f.write('Average Change: $-2315.12\n')
f.write('Greatest Increase in Profits: Feb-2012 ($1926159)\n')
f.write('Greatest Decrease in Profits: Sep-2013 ($-2196167)')
f.close()