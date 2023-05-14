from sqlalchemy.orm import Session
from data.repository.repositories import ProductRepository
from data.dto.schemedto import ProductDTO
from data.models.models import Product

import uuid


class ProductService():
    repository: ProductRepository

    def __init__(self, database: Session):
        self.repository = ProductRepository(database)

    def find_all_products(self, page=0, limit=100):
        products = self.repository.get_products(page, limit)
        return products

    def find_product_by_id(self, product_id: str):
        return self.repository.get_product_by_id(product_id)

    def create_product(self, product: ProductDTO):
        print(product)
        return self.repository.create_product(Product(id=str(uuid.uuid4()), name=product.name, price=product.price, stock=product.stock))
