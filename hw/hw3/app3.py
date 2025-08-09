from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#  экземпляр движка для подключения к SQLite базе данных в памяти
engine = create_engine('sqlite:///:memory:')
print("движок для SQLite создан")

#  сессия для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()
print("сессия успешно создана")

# модели Product,Category, установка связи между ними
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
        return f"<Product(id='{self.id}', name='{self.name}', price='{self.price}')>"


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id='{self.id}', name='{self.name}')>"


Base.metadata.create_all(engine)
print("модели и таблицы созданы")