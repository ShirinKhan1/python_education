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
    query3 = """
    SELECT supplier_id, MAX(unit_price) AS max_price
    FROM products
    WHERE supplier_id IN (1, 3, 5)
    GROUP BY supplier_id
    ORDER BY supplier_id;
    """

    try:
        # Подключение к базе данных
        with psycopg2.connect(**connection_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query1)
                results1 = cursor.fetchall()
                cursor.execute(query2)
                results2 = cursor.fetchall()
                cursor.execute(query3)
                results3 = cursor.fetchall()

        # Вывод результатов
        print("Продукты с ценой от 3 до 7:")
        for row in results1:
            print(row[0])
        if results2:
            print(f"Цена самого дешевого товара в категории 1: {results2[0]}")
        else:
            print("Нет товаров в категории 1.")
        if results3:
            print("Максимальная цена по поставщикам:")
            for row in results3:
                print(f"Supplier ID: {row[0]}, Max Price: {row[1]}")
        else:
            print("Нет данных для поставщиков с id 1, 3, 5.")

    except psycopg2.Error as e:
        print(f"Ошибка подключения или выполнения запроса: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")

# Запуск функции
if __name__ == "__main__":
    fetch_products_in_price_range()
