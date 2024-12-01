import psycopg2

def fetch_products_in_price_range():
    # Данные для подключения
    connection_params = {
        "host": "95.163.241.236",
        "port": 5432,
        "dbname": "nordwind",
        "user": "student",
        "password": "qweasd963"
    }

    query1 = """
    SELECT product_name
    FROM products
    WHERE unit_price >= 3 AND unit_price < 7;
    """
    query2 = """
    SELECT MIN(unit_price) AS min_price
    FROM products
    WHERE category_id = 1;
    """

    try:
        # Подключение к базе данных
        with psycopg2.connect(**connection_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query1)
                results1 = cursor.fetchall()
                cursor.execute(query2)
                results2 = cursor.fetchall()

        # Вывод результатов
        print("Продукты с ценой от 3 до 7:")
        for row in results1:
            print(row[0])
        if results2:
            print(f"Цена самого дешевого товара в категории 1: {results2[0]}")
        else:
            print("Нет товаров в категории 1.")

    except psycopg2.Error as e:
        print(f"Ошибка подключения или выполнения запроса: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")

# Запуск функции
if __name__ == "__main__":
    fetch_products_in_price_range()
