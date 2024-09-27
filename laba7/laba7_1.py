import threading

# Функция для записи в текстовый файл
def write_to_file(lock, file_name, content):
    lock.acquire()  # Захватываем lock перед записью в файл
    try:
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(content + '\n')
    finally:
        lock.release()  # Освобождаем lock

# Создаем lock для управления доступом к файлу
lock = threading.Lock()
# Создаем два потока для записи в файл
t1 = threading.Thread(target=write_to_file, args=(lock, 'price_list.txt', 'Футболка, штуки'))
t2 = threading.Thread(target=write_to_file, args=(lock, 'price_list.txt', 'Носки, пары'))
t1.start()
t2.start()
t1.join()
t2.join()

print("Данные записаны в файл price_list.txt")
