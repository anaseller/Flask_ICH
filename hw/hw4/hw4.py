import os
from decimal import Decimal
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey, Text, func, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///products.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric)
    in_stock = Column(Boolean)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id='{self.id}', name='{self.name}', price='{self.price}', category='{self.category.name}')>"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id='{self.id}', name='{self.name}')>"

Base.metadata.create_all(engine)



print("\n--- Задача 1: Наполнение данными ---")

with Session() as session:
    if session.query(Category).count() == 0:
        category_electronics = Category(name="Электроника", description="Гаджеты и устройства.")
        category_books = Category(name="Книги", description="Печатные книги и электронные книги.")
        category_clothing = Category(name="Одежда", description="Одежда для мужчин и женщин.")

        session.add_all([category_electronics, category_books, category_clothing])
        session.flush()

        products = [
            Product(name="Смартфон", price=Decimal("299.99"), in_stock=True, category=category_electronics),
            Product(name="Ноутбук", price=Decimal("499.99"), in_stock=True, category=category_electronics),
            Product(name="Научно-фантастический роман", price=Decimal("15.99"), in_stock=True, category=category_books),
            Product(name="Джинсы", price=Decimal("40.50"), in_stock=True, category=category_clothing),
            Product(name="Футболка", price=Decimal("20.00"), in_stock=True, category=category_clothing)
        ]
        session.add_all(products)
        session.commit()
        print("Данные успешно добавлены")
    else:
        print("Данные уже существуют")


    print("\n--- Задача 2: Чтение данных ---")
    all_categories = session.execute(select(Category)).scalars().all()
    for category in all_categories:
        print(f"\nКатегория: {category.name}")
        for product in category.products:
            print(f"  - Продукт: {product.name}, Цена: {product.price}")


    print("\n--- Задача 3: Обновление данных ---")
    stmt = select(Product).where(Product.name == "Смартфон")
    product = session.execute(stmt).scalars().first()
    if product:
        print(f"Старая цена 'Смартфон': {product.price}")
        product.price = Decimal("349.99")
        session.commit()
        print(f"Новая цена 'Смартфон': {product.price}")



    print("\n--- Задача 4: Агрегация и группировка ---")
    product_counts = session.execute(
        select(Category.name, func.count(Product.id)).
        join(Product).
        group_by(Category.name)
    ).all()

    for category_name, count in product_counts:
        print(f"В категории '{category_name}' - {count} продукт(ов).")


    print("\n--- Задача 5: Группировка с фильтрацией ---")
    filtered_counts = session.execute(
        select(Category.name, func.count(Product.id)).
        join(Product).
        group_by(Category.name).
        having(func.count(Product.id) > 1)
    ).all()

    for category_name, count in filtered_counts:
        print(f"Категория '{category_name}' содержит более одного продукта: {count}")