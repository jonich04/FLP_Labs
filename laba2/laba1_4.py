# Ввод строки и слова для поиска
sentence = input("Введите строку: ")
search_word = input("Введите слово для поиска: ")
if search_word in sentence:
    print(f"Слово '{search_word}' найдено в строке.")
else:
    print(f"Слово '{search_word}' не найдено.")
