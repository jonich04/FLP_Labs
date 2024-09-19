sentence = input("Введите строку, разделенную пробелами: ")
# Поиск самого длинного слова с использованием генератора списков
longest_word = max([word for word in sentence.split()], key=len)
print(f"Самое длинное слово: {longest_word}")
