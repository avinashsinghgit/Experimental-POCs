from fastapi import FastAPI
import uvicorn
from presentation.routes.product_routes import product_router


app = FastAPI(
    title="DDD+TDD+Clean API's",
    descrption="A POC on DDD+TDD+Clean arhcetecture with FastAPI",
    version="1.0.0"
)


app.include_router(product_router, prefix="/api/v1", tags=["Product"])


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8086, reload=True)

if __name__ == "__main__":
    main()