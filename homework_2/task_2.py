class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        """
        Добавляет данные в буфер. Если в буфере уже 5 или больше элементов, очищает буфер.
        """
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Переполнение буфера. Буфер очищен.")
            self.buffer.clear()

    def get_data(self):
        """
        Возвращает данные из буфера. Если буфер пуст, сообщает об этом.
        """
        if not self.buffer:
            print("Буфер пуст. Данных нет.")
        else:
            print(f"Текущие данные в буфере: {self.buffer}")
            return self.buffer

buffer = DataBuffer()

# Добавляем данные в буфер
buffer.add_data(1)
buffer.add_data(2)
buffer.get_data()  # Выведет: [1, 2]

buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)  # Переполнение буфера. Буфер очищен.

buffer.get_data()  # Выведет: Буфер пуст. Данных нет.
