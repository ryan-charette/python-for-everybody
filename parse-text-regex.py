#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text.
#The numbers can appear anywhere in the line. 
#There can be any number of numbers in each line (including none).
#The basic outline of this problem is to:
    #read the file
    #look for integers using re.findall()
    #look for a regular expression of '[0-9]+'
    #convert the extracted strings to integers
    #sum up the integers

import re

name = input("Enter file:")
handle = open(name)

numbers = re.findall('[0-9]+', handle.read())

sum = 0
for number in numbers:
    sum = sum + int(number)
print(sum) 