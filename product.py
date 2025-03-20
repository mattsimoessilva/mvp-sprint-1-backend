class Product:
    
    def __init__(self, name: str, price: float, category: str, description: str, stock: int) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.stock = stock