note = ["username","titles", "content", "satus", "current_date","issue_date"]
note[0]=input('введите имя пользователя: ') #ввод имени пользователя
count=input("скколько заметок Вы хотите сделать? ")
title1=input('введите заголовок заметки: ') # Ввод заголовка
title2=input('введите 2-ой заголовок заметки: ')
title3=input('введите 3-й заголовок заметки: ')
note[1]=[title1,title2,title3]
note[2]=input('введите пункты заметки: ')
note[3]=('в работе')
note[4]=input('введите дату (в формате DD-MM-YYYY) начала выполнения заметки: ')
note[5]=input('введите окончательную дату (в формате DD-MM-YYYY) для завершения замметки: ')
print(note)