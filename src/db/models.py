import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Relationship


class Base(DeclarativeBase, AsyncAttrs):
    pass


class TimeStampedBase(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(DateTime, onupdate=datetime.datetime.now(datetime.UTC))


class User(TimeStampedBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)

    api_keys = Relationship("ApiKeys", back_populates="user", passive_deletes=True)

    def __repr__(self):
        return f"[{self.id}] {self.username}"


class ApiKeys(TimeStampedBase):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    key = Column(String, unique=True, nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )

    user = Relationship("User", back_populates="api_keys")

    def __repr__(self):
        return f"[{self.id}] {self.key}"
