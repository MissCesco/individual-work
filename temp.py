import datetime
year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

birthyear = int(input("What is your birth year?"))
birthmonth =int(input("What is your birth month?"))
birthday = int(input("What is your birth day?"))

if month < 6:
    grade = True
elif month == 6 and day <= 15:
    grade = True
elif month == 9 and day > 1:
    grade = True
elif month > 9:
    grade = True
else:
    grade = False

year_diff = year-birthyear
if month < birthmonth:
    year_diff -= 1
if month == birthmonth and day<birthday:
    year_diff -= 1

if grade == True:
    grade = year_diff-5
else:
    grade = year_diff-6

print("You are in grade", grade)

