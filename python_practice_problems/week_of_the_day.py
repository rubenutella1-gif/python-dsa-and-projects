week_days = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wednesday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday"
}

while True:
    day = week_days.get(input("Enter the week number (1–7): "), "Invalid input! Please enter a number from 1 to 7.")
    print(day)