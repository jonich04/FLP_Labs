from datetime import datetime
date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
date_obj = datetime.strptime(date_str, '%d.%m.%Y')
month_name = date_obj.strftime('%B')
day = date_obj.day  # Номер дня без лидирующих нулей
year = date_obj.year
formatted_date = f"{month_name} {day}, {year}"
print("Форматированная дата:", formatted_date)
