import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    """
    Получает данные с указанного URL и парсит HTML-код.
    :param url: URL веб-страницы
    """
    try:
        # Получение данных с веб-сайта
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа
        
        # Парсинг HTML-кода
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Извлечение заголовка страницы
        title = soup.title.string if soup.title else "Заголовок отсутствует"
        print(f"Заголовок страницы: {title}")
        
        # Извлечение всех ссылок
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print(f"Найдено {len(links)} ссылок:")
        for link in links[:10]:  # Вывод первых 10 ссылок
            print(link)
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")

# Пример использования
if __name__ == "__main__":
    url = "https://rostov.cian.ru/"
    fetch_and_parse(url)
