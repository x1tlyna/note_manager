from datetime import datetime, timedelta #импортирууем модуль времени. datetime - получение текущего времени, timedelta - класс операций со временем
current_datetime = datetime.now() # текущая дата со временем, вплоть до миллисекунд
created_date=current_datetime.date() # присвоение переменной толькко даты без времени
issue_date=created_date + timedelta(days=1) # присвоение переменной даты с прибавкой 1 дня


username=('Sasuke')
print("ваше имя - ",username)
print('введите заголовок заметки')
title=('дела на день') # Ввод заголовка
print('название заголовкка - ',title)
content=('сделать дела, которы давно надо сделать')
print('ваше описание заметкки - ', content)
status=('в работе')
print('статус заметки', status)
print('дата создания заметки: ',created_date)
print('дата закрытия заметки: ', issue_date)