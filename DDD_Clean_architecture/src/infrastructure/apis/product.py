
import requests
from fastapi import HTTPException

class ProductAPIs:
    def __init__(self):
        self.product_api_url = "https://dummyjson.com/products"

    def get_products_list(self):
        try:
            response = requests.get(self.product_api_url)
            if response.status_code!=200:
                return HTTPException(status_code=500, detail="Unable to fetch products list")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_product_with_id(self,product_id):
        try:
            product_id_url = f"{self.product_api_url}/{product_id}"
            response = requests.get(product_id_url)
            if response.status_code!=200:
                raise HTTPException(status_code=404, detail="Product not found")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
