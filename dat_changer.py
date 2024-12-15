from datetime import datetime, timedelta #импортирууем модуль времени. datetime - получение текущего времени, timedelta - класс операций со временем
current_datetime = datetime.now() # текущая дата со временем, вплоть до миллисекунд
created_date=current_datetime.date() # присвоение переменной толькко даты без времени
issue_date=created_date + timedelta(days=1) # присвоение переменной даты с прибавкой 1 дня
str_date=str(created_date)
print('просто дата', str_date)
print('дата без года', str_date[5:10])
print('дата без дня', str_date[0:7])
print('дата без месяца и года', str_date[8:10])
