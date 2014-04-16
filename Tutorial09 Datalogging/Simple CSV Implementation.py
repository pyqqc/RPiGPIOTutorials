#!/usr/bin/env python

#What the output looks like in Excel: http://s19.postimg.org/npvm4ns4z/Simple_CSV_test.png
#What the output looks like in Notepad: http://s19.postimg.org/3jwpjilv7/Simple_CSV_test_notepad.png

#Import the CSV module
import csv

#Open the CSV file. 'w+' will create file if it doesn't already exist
outputfile = open('csvTestFile.csv', 'w+')

#If using Python older than version 3 and using Windows, uncomment the line below
#outputfile = open('csvTestFile.csv', 'w+b')

#Object used to write to the file
writer = csv.writer(outputfile)

#Write the header row, this could be [currentDate, currentTime, value1, value2] or whatever
writer.writerow(['header1','header2','header3', 'header4'])

#Replace this with your actual loop
for i in range(0,9):
    writer.writerow(['data', 'more data', 'this is row number ->', str(i)])

#Remember to close your file after you are done with it
outputfile.close()

#Just to tell you when it is finished
print('Done')
