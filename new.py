calculator
def calculate(expression):
    # Заменяем минус на "плюс минус" для упрощения парсинга
    expression = expression.replace('-', '+-')
    
    # Если выражение начинается с +, удаляем его
    if expression.startswith('+'):
        expression = expression[1:]
    
    # Разбиваем выражение по + и суммируем числа
    numbers = expression.split('+')
    
    # Преобразуем строки в числа и суммируем
    result = sum(int(num) for num in numbers if num)
    
    return result

# Проверка на примере
test_expression = "1+22-3+4-5+123"
print(calculate(test_expression))  # Должно вывести 142

slice
def string_operations(s):
    results = []
    
    # 1. Третий символ строки
    results.append(s[2])
    
    # 2. Предпоследний символ строки
    results.append(s[-2])
    
    # 3. Первые пять символов строки
    results.append(s[:5])
    
    # 4. Строка без последних двух символов
    results.append(s[:-2])
    
    # 5. Символы с чётными индексами
    results.append(s[0::2])
    
    # 6. Символы с нечётными индексами
    results.append(s[1::2])
    
    # 7. Строка в обратном порядке
    results.append(s[::-1])
    
    # 8. Символы через один в обратном порядке, начиная с последнего
    results.append(s[::-2])
    
    # 9. Длина строки
    results.append(str(len(s)))
    
    return results

# Проверка на примере
test_string = "Abrakadabra"
results = string_operations(test_string)

for result in results:
    print(result)
