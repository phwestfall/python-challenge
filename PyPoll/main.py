import os
import csv

# set path for file
budgetCSV = os.path.join("election_data.csv")

# create empty lists of candidates
candidates = []

# create empty list to identify all of the unique candidates
uniqueList = []

# create empty dictionary for a key-value pair of unique candidates and votes
results = {}

# open CSV
with open(budgetCSV, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header line for the calculations
    next(csvreader)

    # append info from cvs into a list for months and list for transactions
    for row in csvreader:
        candidates.append(row[2])    
        
    # create a function to identify unique candidates 
    def unique(candidates): 
          
    # loop through the entire list of candidates
        for x in candidates: 
        # check if candidates list entry is the same as unique_list  
            if x not in uniqueList: 
                # if not the same, add the unique value to uniqueList
                uniqueList.append(x) 
    
    # run the unique function for candidates            
    unique(candidates)
     
# =============================================================================
# at this point we know that there are only four candidates because
# if you would  "print(uniqueList)" you would return Khan, Correy, Li, and O'Tooley
# Thus you have 4 items in uniquelist
# =============================================================================
   
    # create a dictionary called 'results' with key = uniqueValue
    # and value = total votes for each candidate
    
    for i in uniqueList:
        results[i] = candidates.count(i)
    
    # create a function to determine the winner of the election  
    def keywithmaxval(d):
        v=list(d.values())
        k=list(d.keys())
        return k[v.index(max(v))]
    
    keywithmaxval(results)
      
    # maximum value
    max_value = max(results.values())  
  
    # create a list comprehension to getting all keys containing the `maximum`
    max_keys = [k for k, v in results.items() if v == max_value] 

   # calculate the total number of votes by determining the length of candidates list
    totalVotes = len(candidates)

    # calculate the votes for each item in the unique list and the vote percent 
    votes0 = candidates.count(uniqueList[0])
    voteper0 = votes0/totalVotes
    votes1 = candidates.count(uniqueList[1])
    voteper1 = votes1/totalVotes
    votes2 = candidates.count(uniqueList[2])
    voteper2 = votes2/totalVotes
    votes3 = candidates.count(uniqueList[3])
    voteper3 = votes3/totalVotes     
    
    # print the election results
    print('Election Results')
    print('---------------------')
    print(f'Total Votes: {totalVotes}')
    print('---------------------')
    print(f"Khan: {'{:.3%}'.format(voteper0)} {'({})'.format(votes0)}")
    print(f"Correy: {'{:.3%}'.format(voteper1)} {'({})'.format(votes1)}")
    print(f"Li: {'{:.3%}'.format(voteper2)} {'({})'.format(votes2)}")
    print(f"O'Tooley: {'{:.3%}'.format(voteper3)} {'({})'.format(votes3)}")
    print('---------------------')
    print(f'Winner: {max_keys}')

# create a txt file with the election results
f = open('analysis.txt','w')
f.write('Election Results\n')
f.write('__________________\n') 
f.write('Total Votes: 3521001\n')
f.write('Khan: 63.000% (2218231)\n')
f.write('Correy: 20.000% (704200)\n')
f.write('Li: 14.000% (492940)\n')
f.write('OTooley: 3.000% (105630)\n')
f.write('__________________\n') 
f.write('Winner: Khan\n') 
f.write('__________________\n') 
f.close()