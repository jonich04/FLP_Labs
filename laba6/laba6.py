from abc import ABC, abstractmethod

# 1. Абстрактный класс с атрибутом number
class AbstractNumber(ABC):
    def __init__(self, number=0):
        self.number = number  # Атрибут для хранения числа

# 2. Класс с методами из первого задания
class NumberFunctions(AbstractNumber):
    def process_number(self):
        if 1 <= self.number <= 3:
            self.repeat_string()
        elif 4 <= self.number <= 6:
            self.raise_to_power()
        elif 7 <= self.number <= 9:
            self.increment_number()
        else:
            self.invalid_input()

    def repeat_string(self):
        s = input("Введите строку: ")
        n = int(input("Введите количество повторений строки: "))
        for _ in range(n):
            print(s)

    def raise_to_power(self):
        m = int(input("Введите степень: "))
        result = self.number ** m
        print(f"Результат возведения {self.number} в степень {m} = {result}")

    def increment_number(self):
        print(f"Увеличиваем число {self.number} на единицу в цикле 10 раз:")
        for i in range(1, 11):
            print(self.number + i)

    def invalid_input(self):
        for _ in range(5):
            print("Ошибка! Введите число от 1 до 9.")

# 3. Конечный класс, который наследует оба класса
class FinalNumberProcessor(NumberFunctions):
    def __init__(self, number=0):
        super().__init__(number)  # Вызов конструктора родительского класса
        self.process_number()  # Обработка числа

# Использование конечного класса
while True:
    try:
        user_input = int(input("Введите число от 1 до 9: "))
        processor = FinalNumberProcessor(user_input)  # Создаем объект конечного класса
    except ValueError:
        print("Ошибка! Введите целое число.")

    if input("Хотите продолжить? (да/нет): ").lower() != 'да':
        break
