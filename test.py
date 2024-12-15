username=input('введите имя пользователя: ') #ввод имени пользователя
count=int(input('сколько заметок Вы хотите создать?:'))
notes=[] # пустой список для заметок
for a in range(count):
    title=input('введите заголовок заметки: ')
    content=input('введите пункты заметки (пункты вводить через запятую): ')
    status=input('введите статус заметки: ')
    current_date=input('введите дату (в формате DD-MM-YYYY) начала выполнения заметки: ')
    issue_date=input('введите окончательную дату (в формате DD-MM-YYYY) для завершения замметки: ')
    note = { #наполнение списка заметокк
        'имя': username,
        'заголовок': title,
        'пункты': content,
        'статус': status,
        'дата начала': current_date,
        'дата окончания': issue_date
    }
    notes.append(note)
print("ваши заметки:")
for note in notes: #вывод всех получившихся заметок
    print(note)
