from datetime import datetime, date

# Получаем текущую дату
current_date = date.today()
formatted_current_date = current_date.strftime('%d-%m-%Y')
print("Текущая дата:", formatted_current_date)

while True:
    # Запрашиваем дату у пользователя
    date_input = input('Введите дату (дд-мм-гггг): ')

    # Преобразуем введённую дату в объект datetime
    try:
        input_date = datetime.strptime(date_input, '%d-%m-%Y').date()  # Извлекаем только дату
        break  # Ввод корректен, выходим из цикла
    except ValueError:
        print("Ошибка: Неправильный формат даты. Пожалуйста, используйте 'дд-мм-гггг'.")

# Вычисление разницы между датами
date_difference = abs((input_date - current_date).days)  # Получаем абсолютное значение разницы в днях

# Вывод результатов
if input_date < current_date:
    print(f"дедлайн просрочен на {date_difference} дней.")
elif input_date > current_date:
    print(f"до дедлайна осталось {date_difference} дней.")
else:
    print("сегодня дедлайн")

print(f"Разница между датами: {date_difference} дней.")  # Просто показываем разницу