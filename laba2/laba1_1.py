sentence = input("Введите строку, разделенную пробелами: ")
# Разделение строки на слова
words = sentence.split()
longest_word = max(words, key=len)
print(f"Самое длинное слово: {longest_word}")
