from datetime import datetime, timedelta
n = int(input("Введите число от 1 до 365: "))
start_of_year = datetime(datetime.now().year, 1, 1)
result_date = start_of_year + timedelta(days=n-1)
print("Дата:", result_date.strftime('%d.%m.%Y'))
