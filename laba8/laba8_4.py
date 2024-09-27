from datetime import datetime
from dateutil.relativedelta import relativedelta
current_date_str = input("Введите текущую дату в формате ДД.ММ.ГГГГ: ")
current_date = datetime.strptime(current_date_str, '%d.%m.%Y')
new_date = current_date - relativedelta(months=1)
new_date_plus_year = new_date + relativedelta(years=1)
day_of_year = new_date_plus_year.timetuple().tm_yday
print("Номер дня через год:", day_of_year)
