import re

def reverse_word_if_at_ends(sentence, symbol):
    words = sentence.split()
    if words[0].startswith(symbol):
        words[0] = words[0][::-1]
    if words[-1].endswith(symbol):
        words[-1] = words[-1][::-1]
    return " ".join(words)

def main():
    while True:
        sentence = input("Введите строку: ")
        symbol = input("Введите символ: ")
        
        result = reverse_word_if_at_ends(sentence, symbol)
        print(f"Результат: {result}")
        
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
