

from pydantic import BaseModel, Field
from decimal import Decimal


class Product(BaseModel):
    name: str
    description: str = Field(default=None, description="Описание товара")
    price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8888.88
    in_stock: bool = Field(default=True, alias="available") # ... -> elipsys


product = Product(
    name="Chair",
    price=Decimal("9.23"),
    available=False
)

print(product)
print(product.price)


