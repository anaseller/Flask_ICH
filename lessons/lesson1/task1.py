from flask import Flask, request

app = Flask(__name__)


# @app.route('/home')
# def hello_world():  # put application's code here
#     return 'Hello World!'

# lesson1. Есть небольшой набор данных. Написать маршрут, который
# возвращает имя по user_id из этого набора данных и
# User not found -- если ничего не найдено.
#

# users = {lesson1: "Alice", 2: "Bob", 3: "Charlie"}
#
# @app.route('/user/<int:user_id>')
# def get_user(user_id):
#     name = users.get(user_id)
#     if name:
#         return name
#     else:
#         return "User not found"

# 2. Написать маршрут, который удаляет элемент из списка data.
# data = ["apple", "banana", "cherry"]
#
# @app.route('/fruits/<string:name>', methods=['DELETE'])
# def delete_item(name):
#     if name in data:
#         data.remove(name)
#         return {"message": "Item successfully deleted"}, 204
#     else:
#         return {"massage": "Item not found"}, 404


# 3. Написать маршрут, который будет принимать роль и действие и возвращать
# True/False по permissions.

# permissions = {
# "admin": ["create", "delete", "update"],
# "editor": ["update"],
# "user": ["read"]
# }

# @app.route('/role/<string:role>/<string:action>') #var1
# def get_permissions(role, action):
#     if action in permissions[role]:
#         return {'allowed': True}
#     else:
#         return {'allowed': False}

#
# # var2
# @app.route('/role/<string:role>/<string:action>')
# def role(role, action):
#     actions = permissions.get(role, [])
#     return {'allowed': action in actions}

# 4. Фильтрация списка по query params
# ТЗ: GET /products
# В products лежит список словарей.
# Поддерживаются query-параметры: min_price, max_price, category.
# Нужно реализовать получение записей по фильтрам церез query params

products = [
{"id": 1, "name": "Chair", "price": 45, "category": "furniture"},
{"id": 2, "name": "Sofa", "price": 120, "category": "furniture"},
{"id": 3, "name": "Laptop", "price": 1000, "category": "electronics"}
]

@app.route('/products')
def get_products():

if __name__ == '__main__':
    app.run()