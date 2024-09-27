from datetime import datetime
date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
date_obj = datetime.strptime(date_str, '%d.%m.%Y')
print("Дата:", date_obj)
