import csv
import threading

# Функция для записи в CSV файл
def write_to_csv(lock, file_name, rows):
    lock.acquire()
    try:
        with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                writer.writerow(row)
    finally:
        lock.release()

lock = threading.Lock()
rows1 = [['Футболка', 'штуки']]
rows2 = [['Носки', 'пары']]
t1 = threading.Thread(target=write_to_csv, args=(lock, 'price_list.csv', rows1))
t2 = threading.Thread(target=write_to_csv, args=(lock, 'price_list.csv', rows2))
t1.start()
t2.start()
t1.join()
t2.join()
print("Данные записаны в файл price_list.csv")
