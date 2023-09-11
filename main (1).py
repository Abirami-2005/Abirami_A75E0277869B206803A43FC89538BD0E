#Leap year

def isLeapyear(year):
    if(year%4==0and year %10!=0)or year %400==00:
      return True
    else:
      return False

year=int(input('enter a year:'))

if  isLeapyear (year):
    print('{}is a leap year.'.format (year))
else:
    print('{}is not a leap year.'.format(year))