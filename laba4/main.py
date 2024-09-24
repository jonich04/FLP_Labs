# main.py
from project_folder.age_package.age_checks import check_kindergarten, check_school, check_college, check_work, check_choice, check_invalid

def main():
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if check_invalid(age):
                print("Ошибка! Это программа для людей!")
            elif check_kindergarten(age):
                print("Вам в детский сад")
            elif check_school(age):
                print("Вам в школу")
            elif check_college(age):
                print("Вам в профессиональное учебное заведение")
            elif check_work(age):
                print("Вам на работу")
            elif check_choice(age):
                print("Вам предоставляется выбор")
        except ValueError:
            print("Ошибка! Введите число.")
        
        if input("Хотите продолжить? (да/нет): ").lower() != 'да':
            break

if __name__ == "__main__":
    main()
