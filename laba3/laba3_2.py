def check_age(age):
    if 0 <= age < 7:
        return "Вам в детский сад"
    elif 7 <= age < 18:
        return "Вам в школу"
    elif 18 <= age < 25:
        return "Вам в профессиональное учебное заведение"
    elif 25 <= age < 60:
        return "Вам на работу"
    elif 60 <= age <= 120:
        return "Вам предоставляется выбор"
    else:
        return "Ошибка! Это программа для людей!"

def main():
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            print(check_age(age))
        except ValueError:
            print("Ошибка! Введите число.")
        
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
