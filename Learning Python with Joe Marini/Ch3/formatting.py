# Formatting Time and Date Output
# ===============================

from datetime import datetime
from string import ascii_lowercase as letters
import pandas as pd

now = datetime.now()


def fdate(letter):
    try:
        return now.strftime('%' + letter)
    except ValueError:
        return '-'


def main():
    # Times and dates can be formatted using a set of predefined string control codes
    # Date Formatting

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print('The date is', now.strftime('%A %d %B %Y'))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print('The time is', now.strftime('%I:%M %p'))
    print('The time is', now.strftime('%H:%M'))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print('The locale datetime is', now.strftime('%c'))
    print('The locale date is', now.strftime('%x'))
    print('The locale time is', now.strftime('%X'))

    df = pd.DataFrame({'letter': list(letters)})
    df['date'] = df['letter'].apply(fdate)
    df['DATE'] = df['letter'].apply(lambda x: x.upper()).apply(fdate)
    df.set_index('letter', inplace=True)

    df.loc[:, 'Comment'] = ''
    df.loc['a', 'Comment'] = 'Weekday'
    df.loc['b', 'Comment'] = 'Month Name'
    df.loc['j', 'Comment'] = 'Days in the year'
    df.loc['x', 'Comment'] = 'Locale'
    
    print(df) 
    
    

if __name__ == "__main__":
    main()
