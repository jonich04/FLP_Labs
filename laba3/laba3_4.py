def power_sequence(*args):
    if not args:
        return "Нет чисел для обработки"
    
    result = [args[0]]  # Первое число остается без изменений
    for i in range(1, len(args)):
        result.append(args[i] ** args[i-1])
    
    return result
print(power_sequence(2, 3, 4, 5))  # 2^1, 3^2, 4^3, 5^4
