from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, validator, ValidationError

app = Flask(__name__)


class Address(BaseModel):
    city: str
    street: str
    house_number: int

    @validator('city')
    def city_must_be_valid(cls, value):
        if len(value) < 2:
            raise ValueError('Город должен содержать минимум 2 символа')
        return value

    @validator('street')
    def street_must_be_valid(cls, value):
        if len(value) < 3:
            raise ValueError('Улица должна содержать минимум 3 символа')
        return value

    @validator('house_number')
    def house_number_positive(cls, value):
        if value <= 0:
            raise ValueError('Номер дома не может быть отрицательным числом')
        return value


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_employed: bool
    address: Address

    @validator('name')
    def name_letters_only(cls, value):
        if len(value) < 2 or not value.replace(' ', '').isalpha():
            raise ValueError('Имя должно состоять только из букв и содержать минимум 2 символа')
        return value

    @validator('age')
    def age_in_valid_range(cls, value):
        if value < 0 or value > 120:
            raise ValueError('Возраст должен быть от 0 до 120 лет')
        return value

    @validator('is_employed')
    def employment_check(cls, value, values):
        age = values.get('age')
        if value and (age is not None) and (age < 18 or age > 65):
            raise ValueError('Если пользователь работает, возраст должен быть от 18 до 65 лет')
        return value


@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        user = User(**data)
        return jsonify(user.dict()), 200
    except ValidationError as e:
        errors = []
        for err in e.errors():
            field = ' -> '.join(str(x) for x in err['loc'])
            message = err['msg']
            errors.append(f'{field}: {message}')
        return jsonify({'errors': errors}), 400



if __name__ == '__main__':
    app.run(debug=True)