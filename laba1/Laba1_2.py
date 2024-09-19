# Вывод названия программы
print("Общество в начале XXI века")

while True:
    # Запрос возраста пользователя
    try:
        age = int(input("Введите ваш возраст: "))
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")
        continue
    if 0 <= age < 7:
        print("Вам в детский сад")
    elif 7 <= age < 18:
        print("Вам в школу")
    elif 18 <= age < 25:
        print("Вам в профессиональное учебное заведение")
    elif 25 <= age < 60:
        print("Вам на работу")
    elif 60 <= age <= 120:
        print("Вам предоставляется выбор")
    elif age < 0 or age > 120:
        for _ in range(5):
            print("Ошибка! Это программа для людей!")
    continue_program = input("Хотите продолжить? (да/нет): ").lower()
    if continue_program != 'да':
        print("Программа завершена.")
        break
