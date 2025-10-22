# infrastructure/mongo_repo.py
from pymongo import MongoClient
from domain.product_entity import Product
from domain.abstract_repository import AbstractRepository

class MongoproductRepository(AbstractRepository):
    def __init__(self, uri="mongodb://localhost:27017", db_name="products_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["products"]

    def add(self, product: Product):
        self.collection.update_one(
            {"product_id": product.product_id},
            {
                "$set": {
                    "customer_name": product.customer_name,
                    "items": product.items,
                    "status": product.status,
                }
            },
            upsert=True
        )

    def get(self, product_id: str) -> Product:
        doc = self.collection.find_one({"product_id": product_id})
        if not doc:
            return None
        product = Product(
            product_id=doc["product_id"],
            customer_name=doc["customer_name"],
            items=doc["items"]
        )
        product.status = doc["status"]
        return product
