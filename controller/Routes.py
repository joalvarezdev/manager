from fastapi import APIRouter
from controller.UserController import user_route
from controller.ProductController import product_routes
from config.database import base, engine

base.metadata.create_all(bind=engine)

routes = APIRouter()

routes.include_router(user_route, prefix="/user", tags=["user"])
routes.include_router(product_routes, prefix="/product", tags=["product"])
