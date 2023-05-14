from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.services import ProductService
from config.database import get_database
from data.dto.schemedto import ProductDTO, Response

product_routes = APIRouter()


@product_routes.get("/")
async def get_message(database: Session = Depends(get_database)) -> Response:
    products = ProductService(database).find_all_products()
    return Response(code=200, status="OK", message="Products obtained correctly", result=products).dict(exclude_none=True)


@product_routes.post("/")
async def create_product(request_body: ProductDTO, database: Session = Depends(get_database)) -> Response:
    product_service = ProductService(database)
    product_service.create_product(request_body)
    return Response(code=200, status="OK", message="Product created successfully").dict(exclude_none=True)


@product_routes.get("/{id}")
async def get_product_by_id(id: str, database: Session = Depends(get_database)) -> Response:
    return Response(code=200, status="OK", message="Product obtained correctly", result=ProductService(database).find_product_by_id(id)).dict(exclude_none=True)
