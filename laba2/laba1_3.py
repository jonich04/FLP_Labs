# Ввод строки и разделяющего знака от пользователя
sentence = input("Введите строку: ")
delimiter = input("Введите разделяющий символ: ")
words = sentence.split(delimiter)
shortest_word = min(words, key=len)
print(f"Самое короткое слово: {shortest_word}")
