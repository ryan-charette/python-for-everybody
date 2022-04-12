#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
if h > 40:
    overtime = h - 40
pay = input("Enter Pay:")
p = float(pay)
print((p * h) + (0.5 * p * overtime))