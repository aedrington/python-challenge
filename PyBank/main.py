import os
import csv

#file path
csvpath = os.path.join('C:/Users/austin.edrington/Desktop/Data_Work/Homework/python-challenge-master/python-challenge/PyBank', 'budget_data.csv')

#reader
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

#months
months = (len(open(csvpath).readlines())-1)
print("Total Months: " + str(months))

#total
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total=0
    for row in csvreader:
        total += (float(row[1]))
print("Total: " + str(total))

#average
average = total/months
print("Average Change: " + str(average))

#greatest
greatest = []
date_g = []
lowest = []
date_l = []
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        greatest.append(float(row[1]))
        if greatest == greatest:
            date_g = row[0]
        lowest.append(float(row[1]))
        if lowest == lowest:
            date_l = row[0]

print("Greatest Increase in Profits: " + str(date_g) + " (" + str(max(greatest)) +")")
print("Greatest Decrease in Profits: " + str(date_l) + " (" + str(min(lowest)) +")")

output_file = os.path.join('C:/Users/austin.edrington/Desktop/Data_Work/Homework/python-challenge-master/python-challenge/PyBank', 'output.txt')

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([(Total Months: {str(months)})])
    writer.writerow([(Total: ${str(total)})])
    writer.writerow([(Average Change: ${str(average)})])
    writer.writerow([("Greatest Increase in Profits: " + str(date_g) + " (" + str(max(greatest)) +")")])
    writer.writerow([("Greatest Decrease in Profits: " + str(date_l) + " (" + str(min(lowest)) +")")])