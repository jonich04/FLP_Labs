def count_items_in_file(file_name):
    count_pieces = 0 
    count_pairs = 0  
    total_pieces_quantity = 0  
    total_pairs_quantity = 0  
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            item_data = line.strip().split(',')
            if len(item_data) >= 3:  
                unit = item_data[1].strip().lower()  
                quantity = int(item_data[2].strip())  
                
                if unit == "штуки":
                    count_pieces += 1
                    total_pieces_quantity += quantity 
                elif unit == "пары":
                    count_pairs += 1
                    total_pairs_quantity += quantity 
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"\nКоличество товаров, считаемых в штуках: {count_pieces}\n")
        file.write(f"Общее количество штук: {total_pieces_quantity}\n")
        file.write(f"Количество товаров, считаемых в парах: {count_pairs}\n")
        file.write(f"Общее количество пар: {total_pairs_quantity}\n")
    
    # Выводим результаты на экран
    print(f"Товары, считаемые в штуках: {count_pieces}")
    print(f"Общее количество штук: {total_pieces_quantity}")
    print(f"Товары, считаемые в парах: {count_pairs}")
    print(f"Общее количество пар: {total_pairs_quantity}")

file_name = 'D:\\5 семестр\\питон\\FLP_Labs\\laba7\\price_list.txt'

count_items_in_file(file_name)
