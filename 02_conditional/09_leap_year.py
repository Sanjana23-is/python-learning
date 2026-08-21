# Q9. Leap Year Checker:
# Determine if a year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

year= int(input("enter the current year: "))

if (year % 400 == 0) or (year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is NOT a leap year")