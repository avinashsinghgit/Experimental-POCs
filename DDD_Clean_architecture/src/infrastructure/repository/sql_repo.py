# infrastructure/sql_repo.py
import sqlite3
from domain.product_entity import Product
from domain.abstract_repository import AbstractRepository

class SqlproductRepository(AbstractRepository):
    def __init__(self, db_path: str = "products.db"):
        self.db_path = db_path
        self._ensure_table_exists()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _ensure_table_exists(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id TEXT PRIMARY KEY,
                customer_name TEXT,
                items TEXT,
                status TEXT
            )
        """)
        conn.commit()
        conn.close()

    def add(self, product: Product):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO products (product_id, customer_name, items, status) VALUES (?, ?, ?, ?)",
            (product.product_id, product.customer_name, ",".join(product.items), product.status)
        )
        conn.commit()
        conn.close()

    def get(self, product_id: str) -> Product:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, customer_name, items, status FROM products WHERE product_id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None
        product = Product(product_id=row[0], customer_name=row[1], items=row[2].split(","))
        product.status = row[3]
        return product
