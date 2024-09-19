from string_operations import find_longest_word

def main():
    while True:
        sentence = input("Введите строку, разделенную пробелами: ")
        longest_word = find_longest_word(sentence)
        print(f"Самое длинное слово: {longest_word}")
        
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
