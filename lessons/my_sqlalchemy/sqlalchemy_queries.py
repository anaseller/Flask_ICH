from typing import List, Optional

from sqlalchemy import Float, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(20), nullable=False)

    users: Mapped[List['User']] = relationship('User', uselist=True, back_populates='role')


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        ForeignKeyConstraint(['role_id'], ['role.id'], name='user_ibfk_1'),
        Index('email', 'email', unique=True),
        Index('role_id', 'role_id')
    )
