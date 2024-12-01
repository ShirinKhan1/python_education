from my_package.math_module import MathOperations

# Пример использования
numbers = [1, 2, 3, 4, 5]
try:
    result = MathOperations.sum_list(numbers)
    print(f"Сумма чисел: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")
