# domain/abstract_repository.py
from abc import ABC, abstractmethod
from domain.product_entity import Product

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def get(self, product_id: str) -> Product:
        pass
