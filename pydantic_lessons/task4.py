from pydantic import BaseModel, EmailStr, HttpUrl, Field
from decimal import Decimal
import typing


class Product(BaseModel):
    name: str
    price: Decimal
    tags: list[str]


class User(BaseModel):
    full_name: str
    age: int
    email: EmailStr
    homepage: HttpUrl # https://
    # products: list[Product] = []  # WRONG!!!!
    products: list[Product] = Field(default_factory=list)


user = User(
    full_name="J. Johanson",
    age=32,
    email="j.johanson@google.com",
    homepage="https://example.com"
)

print(user)

