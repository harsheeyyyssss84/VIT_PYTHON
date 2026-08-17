import calendar

year = int(input("ENTER YEAR: "))
month = int(input("ENTER MONTH: "))

if month > 12:
    print("INVALID INPUT")

else:
    print("\n" , calendar.month(year, month))