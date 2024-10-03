import json

def count_items_in_json(file_name, output_file):
    count_pieces = 0 
    count_pairs = 0  
    total_pieces_quantity = 0  
    total_pairs_quantity = 0 
    
    with open(file_name, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        
        for item in data:
            unit = item["unit"].strip().lower()  
            quantity = int(item["quantity"])  
            
            if unit == "штуки":
                count_pieces += 1
                total_pieces_quantity += quantity
            elif unit == "пары":
                count_pairs += 1
                total_pairs_quantity += quantity
    result = {
        "count_pieces": count_pieces,
        "total_pieces_quantity": total_pieces_quantity,
        "count_pairs": count_pairs,
        "total_pairs_quantity": total_pairs_quantity
    }
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)
    print(f"Товары, считаемые в штуках: {count_pieces}")
    print(f"Общее количество штук: {total_pieces_quantity}")
    print(f"Товары, считаемые в парах: {count_pairs}")
    print(f"Общее количество пар: {total_pairs_quantity}")
input_file = 'D:/5 семестр/питон/FLP_Labs/laba7/price_list.json'
output_file = 'D:/5 семестр/питон/FLP_Labs/laba7/result.json'
count_items_in_json(input_file, output_file)
