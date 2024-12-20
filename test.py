from datetime import datetime, timedelta
current_datetime = datetime.now()


username=input('введите имя пользователя: ') #ввод имени пользователя
count=int(input('сколько заметок Вы хотите создать?:'))

notes=[] # пустой список для заметок

for a in range(count):
    title=input('введите заголовок заметки: ')
    content=input('введите пункты заметки (пункты вводить через запятую): ')
    status=input('введите статус заметки: ')
    created_date=current_datetime.date()
    time=int(input('количество дней на выполнение заметки: '))
    issue_date = created_date + timedelta(days=time)
    note = { #наполнение списка заметокк
        'имя': username,
        'заголовок': title,
        'пункты': content,
        'статус': status,
        'дата создания заметки': created_date.strftime('%d-%m-%Y'),
        'срок выполнения заметки': issue_date.strftime('%d-%m-%Y')
    }
    notes.append(note) # добавления значений в заметки
print("ваши заметки:")
for note in notes: #вывод всех получившихся заметок
    print(f"Имя: {note['имя']}, Заголовок: {note['заголовок']}, Пункты: {note['пункты']}, "
          f"Статус: {note['статус']}, Дата создания: {note['дата создания заметки']}, "
          f"Срок выполнения до: {note['срок выполнения заметки']}")
