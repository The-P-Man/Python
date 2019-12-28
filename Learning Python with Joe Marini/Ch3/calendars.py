# Working with Calendars
# ======================

# import the calendar module
import calendar



# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
c.pryear(2020)
c.prmonth(2020, 1)

# Print all dates for weeks that fall in the January 2020\
for date in c.itermonthdates(2020, 1): print(date, end=' ')

# loop over the days of a month. zeroes mean that the day of the week is in an overlapping month
for day in c.itermonthdays(2020, 1): print(day, end=' ')


# # create an HTML formatted calendar
# hc = calendar.HTMLCalendar(0)
# print(hc.formatmonth(2020, 1))

# The Calendar module provides useful utilities for the given locale, such as the names of days and months in both full and abbreviated forms
for month in calendar.month_name: print(month, end=' ')
for day in calendar.day_name: print(day, end=' ')

# # List of months
# print(list(calendar.month_name))


# Calculate days based on a rule: For example, consider a team meeting on the first Friday of every month. To figure out what days that would be for each month, we can use this script:

year = 2020
month = 2

# Get nested list of dates within weeks
cal = calendar.monthcalendar(year, month)
# Can also use calendar.FRIDAY (== 4)
date = cal[0][4] if cal[0][4] != 0 else cal[1][4]
print('The first Friday is {} {} {}'.format(date, calendar.month_abbr[month], year))
c.prmonth(year, month)






