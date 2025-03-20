from product import Product
from product_repository import ProductRepository

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository
    
    def create_product(self, name: str, price: float, category: str, description: str, stock: int) -> Product:
        
        result = Product(
            name = name,
            price = price,
            category = category,
            description = description,
            stock = stock
        )

        self.repository.save(result)

        return result
