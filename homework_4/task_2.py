import itertools

def infinite_generator(start=0, step=1):
    """
    Создает бесконечный генератор чисел, начиная с заданного значения.
    :param start: Начальное значение (по умолчанию 0)
    :param step: Шаг (по умолчанию 1)
    """
    print("Бесконечный генератор чисел (остановите с помощью Ctrl+C):")
    try:
        for num in itertools.count(start=start, step=step):
            print(num)
    except KeyboardInterrupt:
        print("\nГенератор остановлен пользователем.")

def apply_function_to_iterator(iterable, func):
    """
    Применяет функцию к каждому элементу в итераторе.
    :param iterable: Исходный итератор
    :param func: Функция для применения
    """
    try:
        result = itertools.starmap(func, enumerate(iterable))
        print("Результаты применения функции:")
        for item in result:
            print(item)
    except Exception as e:
        print(f"Ошибка при обработке итератора: {e}")

def merge_iterators(*iterables):
    """
    Объединяет несколько итераторов в один.
    :param iterables: Перечень итераторов
    """
    try:
        merged = itertools.chain(*iterables)
        print("Объединенные итераторы:")
        for item in merged:
            print(item)
    except Exception as e:
        print(f"Ошибка при объединении итераторов: {e}")

# Пример использования
if __name__ == "__main__":
    # Задача 1: Создание бесконечного генератора чисел
    print("### Бесконечный генератор ###")
    infinite_generator(start=1, step=2)

    # Задача 2: Применение функций к каждому элементу в итераторе
    print("\n### Применение функций ###")
    sample_iterable = [1, 2, 3, 4, 5]
    apply_function_to_iterator(sample_iterable, lambda i, x: x ** 2 + i)

    # Задача 3: Объединение нескольких итераторов
    print("\n### Объединение итераторов ###")
    iter1 = [1, 2, 3]
    iter2 = ['a', 'b', 'c']
    iter3 = (True, False, None)
    merge_iterators(iter1, iter2, iter3)
