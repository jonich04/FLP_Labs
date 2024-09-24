import random

def magic_8_ball():
    answers = [
        "Да", "Нет", "Возможно", "Скоро узнаешь", "Точно", 
        "Сомневаюсь", "Определённо", "Попробуй позже", "Не уверен"
    ]
    return random.choice(answers)

def main():
    while True:
        question = input("Задайте вопрос: ")
        if question:
            print(f"{question} — {magic_8_ball()}")
        
        if input("Хотите задать ещё вопрос? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
