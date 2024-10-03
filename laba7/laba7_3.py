import json
import threading

# Функция для записи в JSON файл
def write_to_json(lock, file_name, data):
    lock.acquire()
    try:
        with open(file_name, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    finally:
        lock.release()

lock = threading.Lock()
data1 = [
    {"Название": "Футболка", "Измерение": "штуки"}
]
data2 = [
    {"Название": "Носки", "Измерение": "пары"}
]
t1 = threading.Thread(target=write_to_json, args=(lock, 'price_list.json', data1))
t2 = threading.Thread(target=write_to_json, args=(lock, 'price_list.json', data2))
t1.start()
t2.start()
t1.join()
t2.join()

print("Данные записаны в файл price_list.json")
