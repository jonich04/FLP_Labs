class AgeProcessor:
    def __init__(self, age):
        self.age = age  # Введенный возраст
        self.process_age()  # Обрабатываем возраст при создании объекта

    def process_age(self):
        if self.age < 0 or self.age > 120:
            self.invalid_age()
        elif 0 <= self.age < 7:
            self.kindergarten()
        elif 7 <= self.age < 18:
            self.school()
        elif 18 <= self.age < 25:
            self.college()
        elif 25 <= self.age < 60:
            self.work()
        elif 60 <= self.age <= 120:
            self.choice()

    def kindergarten(self):
        print("Вам в детский сад.")

    def school(self):
        print("Вам в школу.")

    def college(self):
        print("Вам в профессиональное учебное заведение.")

    def work(self):
        print("Вам на работу.")

    def choice(self):
        print("Вам предоставляется выбор.")

    def invalid_age(self):
        for _ in range(5):
            print("Ошибка! Это программа для людей.")

# Использование класса
while True:
    try:
        user_age = int(input("Введите ваш возраст: "))
        age_processor = AgeProcessor(user_age)  # Создаем объект класса
    except ValueError:
        print("Ошибка! Введите целое число.")

    if input("Хотите продолжить? (да/нет): ").lower() != 'да':
        break
