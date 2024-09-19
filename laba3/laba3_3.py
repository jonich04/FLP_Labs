def split_and_show(sentence):
    for word in sentence.split():
        print(f"{word} - {len(word)}")
sentence = input("Введите строку: ")
split_and_show(sentence)
