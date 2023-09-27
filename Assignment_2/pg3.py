def leap_year(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

def days_in_month(month, year=1990):
    if month == 2:
        return 28 + int(leap_year(year))
    elif (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        return 31
    else:
        return 30

def date_value(day, month, year):
    value, m = 0, 1
    while m < month:
        value += days_in_month(m, year)
        m += 1
    return value

def date_to_week_day(date, month, year):
    ref_date, input_date = date_value(1, 1, 2006), date_value(date, month, year)
    diff = (input_date - ref_date) % 7
    return diff

def calendar(month, year):
    num_days_mon, day = days_in_month(month, year), date_to_week_day(1, month, year)
    print("SUN \t MON \t TUE \t WED \t THU \t FRI \t SAT")
    for _ in range(day):
        print("", end="\t")
    for i in range(1, num_days_mon + 1):
        print(" ", i, end="\t")
        day += 1
        if day == 7:
            print("")
            day = 0

month, year = input("Enter the month and year: ").split()
calendar(int(month), int(year))