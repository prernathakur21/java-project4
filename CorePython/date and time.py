# Write a Python program using the datetime module to:
# 1. Display the date 7 days from today.
# 2. Display the date 7 days before today.
# import  datetime
#
# today=datetime.date.today()
# future=today+datetime.timedelta(days=7)
# past=today-datetime.timedelta(days=7)
#
# print("7 days from today:",future)
# print("7 days before today:",past)

# Write a Python program using the datetime module to calculate and display a person's current age from their date of birth.
# import datetime
#
# dob = datetime.date(1993, 4, 8)
# today = datetime.date.today()
# age = today.month - today.day
# if (today.month, today.day) < (dob.month, dob.day):
#     age -= 1
# print('your age', age)

# import  datetime
# dob=datetime.date(2000,7,25)
# today=datetime.date.today()
# age=today.year-dob.year
# if(today.month,today.days)<(dob.month,dob.days)
#     age-=1
#
# print("Your age is:", age)

# current date show karne ke liye

# import datetime
# today=datetime.date.today()
# print( 'today date:',today)


# Ye code current date & time nikalne aur current day ka naam print karne ke liye hai.
# import datetime
# now=datetime.datetime.now()
# print('day:',now.strftime("%A"))
# print('day:',now.strftime("%a"))
#
#
# current time show karna hai
# import datetime
# now=datetime.datetime.now()
# print("current time:",now.time())


# current date time year month
# import datetime
# today=datetime.date.today()
# print('today:',today)
#
# print('day:',today.day)
# print('month:',today.month)
# print('year:',today.year)

# Write a Python program using the datetime module to display today's date and then display the same date in the DD-MM-YYYY format.

# import datetime
# today=datetime.date.today()
# print("without formated today:",today)
#
# formatted =today.strftime("%d-%m-%y")
# print("formatted today:",formatted)


# Write a Python program to display your date of birth and the day of the week.
# import datetime
# my_date=datetime.date(1993,4,8)
# print("my_date:",my_date)
# print("my_date of birth day:",my_date.strftime("%A"))

# import datetime
#
# dob = datetime.date(2004,11 ,9)
# today = datetime.date(2026, 10, 8)
#
# age = today.year - dob.year
#
# if (today.month, today.day) < (dob.month, dob.day):
#     age -= 1
#
# print("your age", age)