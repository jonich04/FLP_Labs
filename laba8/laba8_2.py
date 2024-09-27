from datetime import datetime
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
date_obj = datetime(year, month, day)
print("Дата:", date_obj)
