import datetime

date_function = datetime.datetime.now()
time_function = datetime.datetime.now()
day = date_function.strftime('%d')
month = date_function.strftime('%m')
year = date_function.strftime('%Y')
hour = time_function.strftime('%H')

print(type(day))