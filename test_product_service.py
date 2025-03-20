import pytest
from unittest.mock import MagicMock
from hypothesis import given 
import hypothesis.strategies as st
from product_service import ProductService

class TestProductService:

    @given(
        name=st.text(min_size=1, max_size=50),
        price=st.floats(min_value=0.01, max_value=10000),
        category=st.text(min_size=1, max_size=30),
        description=st.text(min_size=0, max_size=200),
        stock=st.integers(min_value=0, max_value=1000)
    )
    def test_create_product(self, name, price, category, description, stock):

        product_repository = MagicMock()
        product_service = ProductService(repository=product_repository)

        product = product_service.create_product(
            name = name,
            price = price,
            category = category,
            description = description,
            stock = stock
        )

        assert product.name == name
        assert product.price == price
        assert product.category == category
        assert product.description == description
        assert product.stock == stock  
