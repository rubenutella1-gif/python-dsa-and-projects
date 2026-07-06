# Check for Leap Year
# Determine if a year is a leap year.
while True:
    year=int(input("Enter Year"))
    if year%4==0 and (year%100!=0 or year%400==0):
        print(f"The year {year} is leap year")
    else:
        print(f"{year} is not a leap year")