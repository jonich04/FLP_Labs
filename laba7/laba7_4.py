import os
import json
import threading

def get_directory_structure(root_dir):
    directory_structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        relative_path = os.path.relpath(dirpath, root_dir)
        directory_structure[relative_path] = {
            "directories": dirnames,
            "files": filenames
        }
    return directory_structure

def save_directory_structure(lock, root_dir, output_file):
    lock.acquire()
    try:
        structure = get_directory_structure(root_dir)
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(structure, jsonfile, ensure_ascii=False, indent=4)
    finally:
        lock.release()

lock = threading.Lock()
root_directory = 'D:\5 семестр\питон\price_list.json'
t1 = threading.Thread(target=save_directory_structure, args=(lock, root_directory, 'directory_structure.json'))
t1.start()
t1.join()

print(f"Структура папки сохранена в файл directory_structure.json")
