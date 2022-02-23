#using pandas
#import pandas
#result = pandas.read_csv('sparshlog.csv')
#print(result)

#using csv
import csv
with open('sparshlog.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        print(line)