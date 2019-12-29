# Working with Calendars
# ======================

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
print('The 2020 Calendar')
c.pryear(2020)
print()

print('The January 2020 Calendar')
c.prmonth(2020, 1)
print()

# Print all dates for weeks that fall in the January 2020
print('All the dates in January 2020')
for date in c.itermonthdates(2020, 1): 
    print(date, end=' ')
print('\n')

# loop over the days of a month. zeroes mean that the day of the week is in an overlapping month
print('All the days in January 2020')
for day in c.itermonthdays(2020, 1): 
    print(day, end=' ')
print('\n')

# # create an HTML formatted calendar
# hc = calendar.HTMLCalendar(0)
# print(hc.formatmonth(2020, 1))

# The Calendar module provides useful utilities for the given locale, such as the names of days and months in both full and abbreviated forms
print('Print the months of the year')
print(list(calendar.month_name))
print('\n')

print(list(calendar.day_name))
print()
# # List of months
# print(list(calendar.month_name))


# A team meet on the first Friday of every month. What day is that in January?

# Get nested list of dates within weeks
cal = calendar.monthcalendar(2020, calendar.January)
# Can also use calendar.FRIDAY (== 4)
date = cal[0][4] if cal[0][4] != 0 else cal[1][4]
print('The first Friday is', date)
print('See for yourself')
c.prmonth(2020, calendar.January)






