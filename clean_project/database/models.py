from __future__ import annotations
from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .base import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    checked = Column(Boolean, default=True)
    priority = Column(Integer, default=None)
    todo_list_id = Column(ForeignKey("todo_list.id"))


class TodoList(Base):
    __tablename__ = "todo_list"
    id = Column(Integer, primary_key=True)

    items: Mapped[List["Item"]] = relationship()
    title = Column(String, index=True)
    owner_id = Column(ForeignKey("owner.id"))
    owner: Mapped[List["Owner"]] = relationship()


class Owner(Base):
    __tablename__ = "owner"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
