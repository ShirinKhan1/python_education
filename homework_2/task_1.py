def read_and_filter_numbers(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()

        for line in data:
            line = line.strip()
            if line.isdigit():
                print(line)
            else:
                raise TypeError(f"Найдена строка с некорректным значением: '{line}'")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except TypeError as e:
        print(f"Ошибка типа: {e}")

read_and_filter_numbers('data.txt')
