from datetime import datetime, timedelta

def display_current_datetime():
    """Отображает текущую дату и время."""
    now = datetime.now()
    print(f"Текущая дата и время: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_date_difference(date1_str, date2_str):
    """
    Вычисляет разницу между двумя датами.
    :param date1_str: Первая дата в формате 'YYYY-MM-DD'
    :param date2_str: Вторая дата в формате 'YYYY-MM-DD'
    """
    try:
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        difference = abs(date2 - date1)
        print(f"Разница между {date1_str} и {date2_str}: {difference.days} дней")
    except ValueError as e:
        print(f"Ошибка: {e}. Убедитесь, что даты введены в формате 'YYYY-MM-DD'.")

def convert_string_to_datetime(date_str):
    """
    Преобразует строку в объект даты и времени.
    :param date_str: Строка с датой и временем в формате 'YYYY-MM-DD HH:MM:SS'
    """
    try:
        dt_object = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        print(f"Строка '{date_str}' преобразована в объект даты и времени: {dt_object}")
    except ValueError as e:
        print(f"Ошибка: {e}. Убедитесь, что дата и время введены в формате 'YYYY-MM-DD HH:MM:SS'.")

# Пример использования
if __name__ == "__main__":
    # Отображение текущей даты и времени
    display_current_datetime()
    
    # Вычисление разницы между двумя датами
    calculate_date_difference("2023-12-01", "2024-01-01")
    
    # Преобразование строки в объект даты и времени
    convert_string_to_datetime("2024-12-01 12:30:45")
