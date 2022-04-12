#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking or bad user data.

hrs = input("Enter Hours:")
pay = input("Enter Hourly Pay:")
print("Pay:" , float(hrs) * float(pay))