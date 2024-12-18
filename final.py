from datetime import datetime, timedelta
current_datetime = datetime.now()
created_date=current_datetime.date()
note = {}

note['username']=input('введите имя пользователя: ') #ввод имени пользователя
count=int(input("сколько заметок Вы хотите сделать? "))

note['created_date']=created_date
note['issue_date']=[]
note['titles']=[]
note['status']=[]
note['content']=[]
for i in range(count):
    title=input(f"введите заголовок заметки {i+1}: ")
    note['titles'].append(title)
    content=input(f'введите пункты заметки: {i+1}: ')
    note['content'].append(content)
    status = input('введите статус заметки ')
    note['status'].append(status)
    time= int(input('количество дней на выполнение заметки: '))
    issue_date = created_date + timedelta(days=time)
    note['issue_date'].append(issue_date.strftime('%d-%m-%Y'))
print("Ваши заметки:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
