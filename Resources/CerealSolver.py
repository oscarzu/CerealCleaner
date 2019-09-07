#Import modules
import os
import csv

#Open the csv
cerealCSV= os.path.join(".","Resources","cereal.csv")
with open(cerealCSV,"r", encoding="UTF-8") as csvfile:
    #create my csv reader
    csvreader= csv.reader(csvfile, delimiter = ",")
    csvHeader = next(csvreader)
    print(f" The header is ¡: {csvHeader}")
    
    for row in csvreader:
        if float (row[7])>= 5:
            print(row)



#Iterate to each rows

#If statement (if the ceral contains 5 or more grams of fiber, print)

#print row if conditions meets