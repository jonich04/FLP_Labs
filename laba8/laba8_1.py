from datetime import datetime
num_date = int(input("Введите дату в формате ГГГГММДД: "))
date_str = str(num_date)
date_obj = datetime.strptime(date_str, '%Y%m%d')
print("Дата:", date_obj)
