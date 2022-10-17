#importing libraries
import os
import csv
from statistics import mean

#set path for file
pybankcsvpath = os.path.join("resources", "budget_data.csv")
#open csv file for reading
file =  open(pybankcsvpath, 'r')

#read csv file
csvreader = csv.reader(file, delimiter=",")

#add header
csv_header = next(csvreader)
#print(f"csv header: {csv_header}")

datelist = []
pllist = []

#visualize data
for row in csvreader:
    #print(row)
    #make list of dates
    datelist.append(row[0])
    pllist.append(int(row[1]))

#test newly created lists
#print(datelist)
#print(pllist)

print("Financial Analysis")
print("___________________________________________________")

#The total number of months included in the dataset
print(f'Total months: {len(datelist)}')

#The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${sum(pllist)}')

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changesinpllist = []
for i in range(len(pllist)-1):
    changesinpllist.append((pllist[i+1])-(pllist[i]))
print(f'Average change: ${round(mean(changesinpllist),2)}')


#The greatest increase in profits (date and amount) over the entire period
greatestincrease = max(changesinpllist)
indgreatestinc = changesinpllist.index(greatestincrease)
dateofgreatestinc = datelist[indgreatestinc + 1]
print(f'Greatest Increase in Profits: {dateofgreatestinc} ({greatestincrease})')

#The greatest decrease in profits (date and amount) over the entire period
lowesttincrease = min(changesinpllist)
indlowestinc = changesinpllist.index(lowesttincrease)
dateoflowtestinc = datelist[indlowestinc + 1]
print(f'Greatest Decrease in Profits: {dateoflowtestinc} ({lowesttincrease})')



file.close()