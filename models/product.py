class Product:
    currency = "USD"

    def __init__(
        self,
        product_id: int,
        name: str,
        description: str,
        price: float,
        stock: int,
        category: str,
    ) -> None:
        # if not isinstance(price, (int, float)) or isinstance(price, bool):
        #     raise TypeError("Price must be a number")
        # if price <= 0:
        #     raise ValueError("Price must be greater than 0")

        # if not isinstance(stock, int) or isinstance(stock, bool):
        #     raise TypeError("Stock must be an integer")
        # if stock < 0:
        #     raise ValueError("Stock cannot be negative")

        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary")
        return cls(
            product_id=data.get("product_id"),
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            stock=data.get("stock"),
            category=data.get("category"),
        )

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self._price = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Stock must be an integer")
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value

    def increase_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        self.stock += quantity

    def decrease_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.stock:
            raise ValueError("Quantity cannot exceed current stock")

        self.stock -= quantity

    def update_price(self, new_price: float) -> None:
        self.price = new_price

    def calculate_discounted_price(self, discount_percent: float) -> float:
        if not isinstance(discount_percent, (int, float)) or isinstance(
            discount_percent, bool
        ):
            raise TypeError("Discount must be a number")
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        return self.price * (1 - discount_percent / 100)

    @property
    def is_available(self) -> bool:
        return self.stock > 0

    def display_info(self) -> None:
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.stock}")
        print(f"Category: {self.category}")
        print(f"Available: {self.is_available}")

    @classmethod
    def change_currency(cls, new_currency: str) -> None:
        if not isinstance(new_currency, str):
            raise TypeError("Currency must be a string.")

        if not new_currency.strip():
            raise ValueError("Currency cannot be empty.")

        cls.currency = new_currency.strip().upper()

    @staticmethod
    def calculate_tax(price: float, tax_rate: float) -> float:
        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
            raise TypeError("Tax rate must be a number")
        if tax_rate < 0 or tax_rate > 100:
            raise ValueError("Tax rate must be between 0 and 100")

        return price * (tax_rate / 100)
