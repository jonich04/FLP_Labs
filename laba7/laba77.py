import csv

def count_items_in_csv(file_name):
    count_pieces = 0  # Счётчик товаров, считаемых в штуках
    count_pairs = 0   # Счётчик товаров, считаемых парами
    total_pieces_quantity = 0  # Общая сумма штук
    total_pairs_quantity = 0  # Общая сумма пар

    with open(file_name, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) >= 3:  # Проверяем, что есть хотя бы три элемента
                unit = row[1].strip().lower()  # Единица измерения
                quantity = int(row[2].strip())  # Количество
                
                if unit == "штуки":
                    count_pieces += 1
                    total_pieces_quantity += quantity
                elif unit == "пары":
                    count_pairs += 1
                    total_pairs_quantity += quantity
    
    print(f"Товары, считаемые в штуках: {count_pieces}")
    print(f"Общее количество штук: {total_pieces_quantity}")
    print(f"Товары, считаемые в парах: {count_pairs}")
    print(f"Общее количество пар: {total_pairs_quantity}")
file_name = 'D:/5 семестр/питон/FLP_Labs/laba7/price_list.csv'
count_items_in_csv(file_name)
