sentence = input("Введите строку, разделенную точкой с запятой: ")
words = sentence.split(';')
longest_word = max(words, key=len)
print(f"Самое длинное слово: {longest_word}")
