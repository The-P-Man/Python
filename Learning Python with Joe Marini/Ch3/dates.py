# Working with Date
# =================

from datetime import date, time, datetime


def main():
    # DATE OBJECTS

    # Get today's date from the date class
    today = date.today()
    print('The date is', today)
    print('The date is', today.strftime('%A, %d %B %Y'))
    
    # Get the different date parts from the date object
    print('The year is', today.year)
    print('The month is', today.month)
    print('The day is', today.day)
    print('The weekday is', today.weekday())

    # The isocalendar method gets the (year, week, dayofweek)
    year, week, dayofweek = today.isocalendar()
    print('The isocalendar year is', year)
    print('The isocalendar week is', week)
    print('The isocalendar weekday is', dayofweek)
    
    # Get today's weekday (0=monday, 6=sunday)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",\
            "Friday", "Saturday", "Sunday"]

    print('The weekday is', days[today.weekday()])
    print()

    # Get today's datetime from the datetime class
    today = datetime.today()
    print('The datetime is', today)
    print()
    # Get the current time
    time = today.time()
    print('The time is', time)
    print('The hour is', time.hour)
    print('The minute is', time.minute)
    print('The second is', time.second)
    print('The microsecond is', time.microsecond)


if __name__ == '__main__':
    main()