from collections import Counter
import string

def count_unique_words(input_string):
    """
    Подсчитывает количество уникальных слов в строке, игнорируя знаки препинания и пробелы.
    :param input_string: строка для анализа
    :return: количество уникальных слов
    """
    # Удаляем знаки препинания
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    
    # Приводим к нижнему регистру и разбиваем на слова
    words = cleaned_string.lower().split()
    
    # Подсчитываем уникальные слова
    word_counts = Counter(words)
    print(f"Уникальные слова: {len(word_counts)}")
    return word_counts

input_text = "Hello, world! Hello, everyone. This is a test: test of unique words."
word_counts = count_unique_words(input_text)

# Вывод
print(f"Количество уникальных слов: {len(word_counts)}")
print("Частота слов:", word_counts)
