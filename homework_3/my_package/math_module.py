class MathOperations:
    @staticmethod
    def sum_list(numbers):
        """
        Вычисляет сумму всех чисел в списке.
        :param numbers: список чисел
        :return: сумма чисел
        """
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Все элементы списка должны быть числами.")
        return sum(numbers)
