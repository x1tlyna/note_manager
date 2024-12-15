from datetime import datetime, timedelta #импортирууем модуль времени. datetime - получение текущего времени, timedelta - класс операций со временем
current_datetime = datetime.now() # текущая дата со временем, вплоть до миллисекунд
created_date=current_datetime.date() # присвоение переменной толькко даты без времени
#issue_date=created_date + timedelta(days=1) # присвоение переменной даты с прибавкой 1 дня


username=input('введите имя пользователя: ') #ввод имени пользователя
title1=input('введите заголовок заметки: ') # Ввод заголовка
title2=input('введите 2-ой заголовок заметки: ')
title3=input('введите 3-й заголовок заметки: ')
titles=[title1,title2,title3]
content=input('введите пункты заметки: ')
status=('в работе')
issue_date=input('введите окончательную дату (в формате DD-MM-YYYY) для завершения замметки: ')
print("ваше имя - ",username)
print('заголовки заметкки - ',titles)
print('вашы пункты заметкки - ', content)
print('статус заметки', status)
print('дата создания заметки: ',created_date)
print('дата закрытия заметки: ', issue_date)