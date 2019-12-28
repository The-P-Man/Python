#
# Example file for working with timedelta objects
#

from datetime import date ,time ,datetime, timedelta

# construct a basic timedelta and print it
delta = timedelta(days=3, hours=2, minutes=1, seconds=30)
print('This is a timedelta', delta)

# print today's date
today = date.today()
print('Today\'s date is', today)

# print today's date one year from now
print('In a year the date will be', today.replace(year=today.year + 1))
# Adding 365 days does not account for leap years
print('In a year the date will be', today + timedelta(days=365), '..assuming no leap year')

# calculate the date 1 week ago, formatted as a string
print('The date a week ago was', today - timedelta(days=7))
print('The date in a week will be', today + timedelta(days=7))

# How many days until Christmas?
xmas = date(today.year, 12, 25)
print('There are', (xmas - today).days ,'days until Christmas')


# How many days until April Fools' Day?
fools = date(today.year, 4, 1)
# If day has been -> next year
if today > fools:
    fools = fools.replace(year=today.year+1)
# Now calculate the amount of time until April Fool's Day  
print('There are', (fools - today).days, 'until April Fools\' Day')



