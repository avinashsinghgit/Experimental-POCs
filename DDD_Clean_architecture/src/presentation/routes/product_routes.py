from fastapi import APIRouter, HTTPException
from domain.product_entity import Product

product_router = APIRouter()

@product_router.get("/", description="Get the list of products")
def get_products_count():
    try: 
        result = Product().product_category_count_avgrating()
        if result is None:
            raise HTTPException(status_code=404, detail="No product found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetvching the product list {e}")

