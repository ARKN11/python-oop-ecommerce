
class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        price: float,
        stock: int,
        category: str,
    ) -> None:
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise ValueError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        if not isinstance(stock, int) or isinstance(stock, bool):
            raise ValueError("Stock must be an integer")
        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    def increase_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        self.stock += quantity

    def decrease_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.stock:
            raise ValueError("Quantity cannot exceed current stock")

        self.stock -= quantity

    def update_price(self, new_price: float) -> None:
        if not isinstance(new_price, (int, float)) or isinstance(new_price, bool):
            raise ValueError("Price must be a number")
        if new_price <= 0:
            raise ValueError("Price must be greater than 0")

        self.price = new_price

    def calculate_discounted_price(self, discount_percent: float) -> float:
        if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
            raise ValueError("Discount must be a number")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        return self.price * (1 - discount_percent / 100)

    def is_available(self) -> bool:
        return self.stock > 0

    def display_info(self) -> None:
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Category: {self.category}")
        print(f"Available: {self.is_available()}")
