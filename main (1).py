def IsLeapYear(year):
  if (year/4 ==0and year/100!=0) or year%400 ==0:
    return True
  else:
    return False
year = int (input("enter the year:"))
if IsLeapYear(year):
  print ("{} is a leap year".format (year))
else:
  print ("{} is not a leap year".format(year))
    
  


  