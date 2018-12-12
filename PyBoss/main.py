
###### only had time to figure out how to split the first name and last name
###### into separate rows 

import os
import csv

# set path for file
budgetCSV = os.path.join("employee_data.csv")

firstlastname = []

# open CSV
with open(budgetCSV, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header line for the calculations
    next(csvreader)

    # append info from cvs into a list for months and list for transactions
    for row in csvreader:
        firstlastname.append(row[1])        
        
    split = [i.split() for i in firstlastname]
    #print(split)
    
    #dateofbirth = ['{}-{}-{}'.format(m,d,y) for y, m, d in map(lambda x: str(x).split('-")), dateofbirth]

output_file = "newEmployeeList.csv"

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile, delimiter=',')
  
    # add the headers
    writer.writerow(["First Name", "Last Name"])

    # add the rest of the rows using the newBudget variable
    writer.writerows(split)
    
    
# =============================================================================
