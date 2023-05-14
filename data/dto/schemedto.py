from pydantic import BaseModel
from typing import Optional, TypeVar, Generic, Union
from pydantic.generics import GenericModel

T = TypeVar("T")


class ProductDTO(BaseModel):

    id: Union[str, None] = None
    name: Union[str, None] = None
    price: Union[float, None] = None
    stock: Union[int, None] = None


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
