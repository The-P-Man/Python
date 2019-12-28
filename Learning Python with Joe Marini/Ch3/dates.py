# Working with Date Information
# ========================================

from datetime import date, time, datetime


def main():
    # DATE OBJECTS

    # get today's date from the date class
    today = date.today()
    print('The date is', today)
    print('The date is', today.strftime('%A, %d %B %Y'))
    
    # Get the different date parts from the date object
    print('The year is', today.year)
    print('The month is', today.month)
    print('The day is', today.day)
    print('The week is', today.isocalendar()[1])
    print('The weekday is', today.weekday())
    
    # Get today's weekday (0=monday, 6=sunday)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",\
            "Friday", "Saturday", "Sunday"]

    print('The weekday is', days[today.weekday()])

    # Get today's date from the datetime class
    today = datetime.today()
    print('The datetime is', today)

    # Get the time
    time = datetime.time(datetime.today())
    print('The time is', time)
    print('The hour is', time.hour)
    print('The minute is', time.minute)
    print('The second is', time.second)


if __name__ == '__main__':
    main()