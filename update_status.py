from datetime import datetime, timedelta
current_datetime = datetime.now()
created_date=current_datetime.date()

note = {}

note['username']=input('введите имя пользователя: ') #ввод имени пользователя
note['titles']=[]
note['status']=[]
note['content']=[]
note['created_date']=[]
note['issue_date']=[]


while True: # цикл добавления заголовков
    title=input(f"введите заголовок заметки или напишите стоп ")

    if title == 'стоп' or title == '':
        break
    elif title.strip() == '':  # Проверка на пустую строку
        print("Ошибка: заголовок не может быть пустым. Пожалуйста, попробуйте снова.")
    else:
        note['titles'].append(title)
if not note['titles']:
    print("Ошибка: вы не ввели ни одного заголовка. Заметка не создана.")
else:
    content=input(f'введите пункты заметки: ')
    note['content'].append(content)

    status = input('введите статус заметки')
    note['status'].append(status)
    date = datetime.now()
    created_date = date.strftime('%d-%m-%Y')
    note['created_date'].append(created_date)

    issue_date = input('введите дату завершения заметки (в формате ДД-ММ-ГГГГ): ')
    note['issue_date'].append(issue_date)

    print(f"Ваши заметки:",note)

# изменение заметки
while True:
    change_status = input('хотите ли вы изменить статус ваших заметок? (да\нет) ' )

    if change_status == 'да':
        print(f'текущий статус заметки:',note['status']) # выбор заметки
        change_status_note = int(input('выбери статус заметки: (1 - выполнено, 2 - в процессе, 3 - отложено): '))# выбор на что менять статус
        # запускаем проверку на выбор
        if change_status_note == 1:
            changed_status = 'выполнено' # присваиваем новый статус заметки
            note['status'] = changed_status
        elif change_status_note == 2:
            changed_status = 'в процессе'
            note['status'] = changed_status
        elif change_status_note == 3:
            changed_status = 'отложено'
            note['status'] = changed_status
        else:
            print('вы ввели неправильно')
            continue # Если статус введён некорректно, пропускаем итерацию

    else:
        break
print(f"Ваши заметки:",note)