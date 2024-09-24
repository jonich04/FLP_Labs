import os
import time

def get_file_info(path):
    try:
        if os.path.exists(path):
            size = os.path.getsize(path)
            creation_time = time.ctime(os.path.getctime(path))
            modification_time = time.ctime(os.path.getmtime(path))
            if os.path.isfile(path):
                file_type = "файл"
            elif os.path.isdir(path):
                file_type = "директория"
            else:
                file_type = "неизвестный тип"
            return {
                "path": os.path.abspath(path),
                "size": size,
                "type": file_type,
                "creation_time": creation_time,
                "modification_time": modification_time
            }
        else:
            return None
    except Exception as e:
        print(f"Ошибка при получении информации о файле: {e}")
        return None

def main():
    while True:
        folder_path = input("Введите путь к папке: ").strip()  # Убираем лишние пробелы
        file_name = input("Введите название файла/папки: ").strip()

        full_path = os.path.join(folder_path, file_name)

        # Проверка, правильно ли указываются пути
        print(f"Проверка пути: {full_path}")
        
        file_info = get_file_info(full_path)
        if file_info:
            print(f"Полный путь: {file_info['path']}")
            print(f"Размер: {file_info['size']} байт")
            print(f"Тип: {file_info['type']}")
            print(f"Дата создания: {file_info['creation_time']}")
            print(f"Дата изменения: {file_info['modification_time']}")
        else:
            print("Файл/папка не найдена.")
        
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
