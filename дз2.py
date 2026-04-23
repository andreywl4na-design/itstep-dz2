# Клас товару
class Product:
    def __init__(self, name, price, stock):
        self.name = name          # Назва товару
        self.price = price        # Ціна
        self.stock = stock        # Кількість на складі

    def show_info(self):
        print(f"Товар: {self.name}, Ціна: {self.price} грн, Наявність: {self.stock} шт.")


# Клас кошика
class Cart:
    def __init__(self):
        self.items = {}   # словник: товар -> кількість

    # Додати товар
    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity

            product.stock -= quantity
            print(f"Додано {quantity} x {product.name}")
        else:
            print(f"Недостатньо товару {product.name} на складі!")

    # Видалити товар
    def remove_product(self, product, quantity=1):
        if product in self.items:
            if self.items[product] <= quantity:
                removed = self.items[product]
                product.stock += removed
                del self.items[product]
                print(f"Товар {product.name} повністю видалено з кошика")
            else:
                self.items[product] -= quantity
                product.stock += quantity
                print(f"Видалено {quantity} x {product.name}")
        else:
            print("Товару немає у кошику")

    # Загальна вартість
    def total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    # Показати кошик
    def show_cart(self):
        print("\nКошик покупця:")
        if not self.items:
            print("Кошик порожній")
        else:
            for product, quantity in self.items.items():
                print(f"{product.name} - {quantity} шт. = {product.price * quantity} грн")
            print(f"Загальна сума: {self.total_price()} грн")


# Створення товарів
p1 = Product("Ноутбук", 25000, 5)
p2 = Product("Мишка", 500, 10)
p3 = Product("Клавіатура", 1200, 7)

# Створення кошика
cart = Cart()

# Робота з кошиком
cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.add_product(p3, 1)

cart.show_cart()

cart.remove_product(p2, 1)

cart.show_cart()