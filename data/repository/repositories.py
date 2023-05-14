from sqlalchemy.orm import Session
from data.models.models import Product


class ProductRepository():
    db: Session

    def __init__(self, db: Session):
        self.db = db

    def get_products(self, page=0, limit=100):
        return self.db.query(Product).offset(page).limit(limit).all()

    def get_product_by_id(self, product_id: str):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
