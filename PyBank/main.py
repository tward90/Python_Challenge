#Import necessary Dependencies
import os
import csv

#Direct to location of data
data = os.path.join("Resources", "budget_data.csv")

#Open data
with open(data, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# Initialize counter totals
    total_months = 0
    total_profit = 0
# Create new PL List for Change Calculations
    pl_list = []
    date_list = []
# Create for loop to assign correct data type as wel as append profit/loss and Date to secondary lists
    for row in csv_reader:
        Profit = int(row["Profit/Losses"])
        pl_list.append(Profit)
        Date = row["Date"]
        date_list.append(Date)
        total_months = total_months + 1
        total_profit = total_profit + Profit

#calculate the average of the month-to-month changes
delta = [j - i for i, j in zip(pl_list[:-1], pl_list[1:])]
total = sum(delta)
avg_delta = total / len(delta)

#Insert Value of 0 to beginning of delta list to account for mising value for first month before zipping
delta.insert(0, 0)

#Create dictionary of months and associated delta's in order to refer to them
date_delta = dict(zip(date_list, delta))

#Find Maximum and Minimum profit in our dictionary
max_key = max(date_delta, key=date_delta.get)
min_key = min(date_delta, key=date_delta.get)

#Print Financial Analysis Table of Findings
print(" ")
print("Financial Analysis")
print("*************************************")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(round(avg_delta,2)))
print("Greatest Increase in Profits: " + max_key + " $" + str(max(delta)))
print("Greatest Decrease in Profits: " + min_key + " $" + str(min(delta)))
print("*************************************")
print(" ")

#Print Financial Analysis Table of Findings to .txt file
#Open correct directory for correct file location
os.chdir("Analysis")
#Append printed lines to new .txt file
print("Financial Analysis", file = open("Financial Analysis.txt", "a"))
print("*************************************", file = open("Financial Analysis.txt", "a"))
print("Total Months: " + str(total_months), file = open("Financial Analysis.txt", "a"))
print("Total: $" + str(total_profit), file = open("Financial Analysis.txt", "a"))
print("Average Change: $" + str(round(avg_delta,2)), file = open("Financial Analysis.txt", "a"))
print("Greatest Increase in Profits: " + max_key + " $" + str(max(delta)), file = open("Financial Analysis.txt", "a"))
print("Greatest Decrease in Profits: " + min_key + " $" + str(min(delta)), file = open("Financial Analysis.txt", "a"))
print("*************************************", file = open("Financial Analysis.txt", "a"))
#Close .txt file
open("Financial Analysis.txt", "a").close()