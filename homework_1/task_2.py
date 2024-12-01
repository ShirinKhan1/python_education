import logging

# Настройка логирования
logging.basicConfig(filename='warehouse.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        self.quantity += amount
        logging.info(f"Увеличено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}.")

    def decrease_quantity(self, amount):
        if amount > self.quantity:
            logging.warning(f"Попытка уменьшить количество товара '{self.name}' на {amount}, но доступно только {self.quantity}.")
            raise ValueError("Недостаточно товара на складе.")
        self.quantity -= amount
        logging.info(f"Уменьшено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}.")

    def total_price(self):
        return self.quantity * self.price


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        logging.info(f"Добавлен товар '{product.name}' на склад. Количество: {product.quantity}, Цена: {product.price}.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                logging.info(f"Удалён товар '{product_name}' со склада.")
                return
        logging.warning(f"Товар '{product_name}' не найден на складе.")

    def total_inventory_value(self):
        total_value = sum(product.total_price() for product in self.products)
        logging.info(f"Общая стоимость товаров на складе: {total_value}.")
        return total_value


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse, product_name, quantity):
        for product in warehouse.products:
            if product.name == product_name:
                try:
                    product.decrease_quantity(quantity)
                    sale_value = quantity * product.price
                    self.sales_report.append((product.name, quantity, sale_value))
                    logging.info(f"{self.name} продал {quantity} единиц товара '{product.name}'. Выручка: {sale_value}.")
                    return sale_value
                except ValueError as e:
                    logging.error(str(e))
                    raise e
        logging.warning(f"Товар '{product_name}' не найден на складе для продажи.")
        raise ValueError("Товар не найден.")

    def sales_summary(self):
        summary = "Отчёт о продажах:\n"
        for item in self.sales_report:
            summary += f"Товар: {item[0]}, Количество: {item[1]}, Выручка: {item[2]}\n"
        logging.info("Сформирован отчёт о продажах.")
        return summary


# Примеры использования

# Создание склада и товаров
warehouse = Warehouse()
apple = Product("Яблоко", 100, 10)
banana = Product("Банан", 150, 5)

# Добавление товаров на склад
warehouse.add_product(apple)
warehouse.add_product(banana)

# Создание продавца
seller = Seller("Алексей")

# Продажа товаров
try:
    seller.sell_product(warehouse, "Яблоко", 10)
    seller.sell_product(warehouse, "Банан", 20)
except ValueError as e:
    print(e)

# Отчёт о продажах
print(seller.sales_summary())

# Общая стоимость товаров на складе
print(f"Общая стоимость товаров на складе: {warehouse.total_inventory_value()}")