from typing import Any

from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Session

from sqlalchemy import engine
from sqlalchemy.db_connector import DBConnector
from sqlalchemy.social_blogs_models import Role, User, News, Comment
from sqlalchemy.social_blogs_schemas import UserResponseSchema, UserCreateSchema



def create_user(session: Session, raw_data: dict[str, Any]) -> UserResponseSchema:
    try:
        validated_data = UserCreateSchema.model_validate(raw_data)

        user = User(**validated_data.model_dump())

        session.add(user)
        session.flush()
        session.refresh(user)
        session.commit()

        return UserResponseSchema.model_validate(user)
    except ValueError as err:
        raise err
    except (IntegrityError, DataError) as db_err:
        session.rollback()
        raise db_err


with DBConnector(engine=engine) as session:
    data = {
        "first_name": "Alex",
        "last_name": "Grey",
        "email": "a.grey@gmail.com",
        "password": "MySecurePassword",
        "repeat_password": "MySecurePassword",
        "phone": "+1 255 777 9999",
        "role_id": 3
    }

    try:
        new_user = create_user(session=session, raw_data=data)

        print("🟢 User Created!")
        print(new_user.model_dump_json(indent=4))
    except Exception as err:
        print(f"Error: {err}")



