from datetime import datetime
current_date_str = input("Введите текущую дату в формате ДД.ММ.ГГГГ: ")
current_date = datetime.strptime(current_date_str, '%d.%m.%Y')
day_of_year = current_date.timetuple().tm_yday
print("Номер дня в году:", day_of_year)
