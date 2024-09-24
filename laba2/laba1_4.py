sentence = input("Введите строку: ")
search_word = input("Введите слово для поиска: ")

words = sentence.split()
if search_word in words:
    position = words.index(search_word) + 1  
    print(f"Слово '{search_word}' найдено в строке на позиции {position} .")
else:
    print(f"Слово '{search_word}' не найдено.")
