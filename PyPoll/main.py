import os
import csv

#file path
csvpath = os.path.join('C:/Users/austin.edrington/Desktop/Data_Work/Homework/python-challenge-master/PyPoll', 'election_data.csv')

#reader
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    correy = []
    khan = []
    li = []
    tooly = []
    for row in csvreader:
        if row[2] == "Correy":
            correy.append((row[2]))
        if row[2] == "Khan":
            khan.append((row[2]))
        if row[2] == "Li":
            li.append((row[2]))
        if row[2] == "O'Tooley":
            tooly.append((row[2]))
total = (len(open(csvpath).readlines())-1)
print("---------------------------------")
print("Total Votes: " + str(total))
print("---------------------------------")

kr = round((len(khan)/total)*100,2)
cr = round((len(correy)/total)*100,2)
lr = round((len(li)/total)*100,2)
tr = round((len(tooly)/total)*100,2)

print("Khan:" + str(kr) +"% (" + str(len(khan))+")")
print("Correy:" + str(cr) +"% (" + str(len(correy))+")")
print("Li:" + str(lr) +"% (" + str(len(li))+")")
print("O'Tooley:" + str(tr) +"% (" + str(len(tooly))+")")
print("---------------------------------")
if kr >= 50:
    print("Winner: Khan")
elif cr >= 50:
    print("Winner: Coorey")
elif lr >= 50:
    print("Winner: Li")
elif tr >= 50:
    print("Winner: O'Tooley")
print("---------------------------------")