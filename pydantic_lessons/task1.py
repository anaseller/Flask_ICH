from pydantic import BaseModel

class Address(BaseModel):
    city: str
    street: str
    house_numb: int
    index: int


class User(BaseModel):
    id: int
    name: str
    age: int
    is_active: bool = True
    address: Address


address = Address(city="Minsk", street="Street", house_numb=13, index=6000)

user = User(id=2, name="Tomas", age=27, address=address)

print(user)

print(user.address.street)