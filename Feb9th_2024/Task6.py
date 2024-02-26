#Leap year checker
year = int(input("Enter the year"))
if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
    print("This is a Leap year",year)
else:
    print("This is not leap year",year)
