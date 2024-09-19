while True:
    # Попросить пользователя ввести число от 1 до 9
    x = int(input("Введите число от 1 до 9: "))
    if 1 <= x <= 3:
        s = input("Введите строку: ")
        n = int(input("Введите количество повторов строки: "))
        for _ in range(n):
            print(s)
            
    elif 4 <= x <= 6:
        m = int(input("Введите степень, в которую возвести число: "))
        result = x ** m
        print(f"{x} в степени {m} равно {result}")
        
    elif 7 <= x <= 9:
        for i in range(10):
            x += 1
            print(x)
            
    else:
        print("Ошибка ввода")
    continue_program = input("Хотите продолжить? (да/нет): ").lower()
    if continue_program != 'да':
        print("Программа завершена.")
        break
