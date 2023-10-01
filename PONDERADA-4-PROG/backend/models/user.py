from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import List
from config.db import base
from .predicted import PredictTable

class UserTable(base):
    __tablename__ = 'user'
    userId = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    predict: Mapped[List["PredictTable"]] = relationship()

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<UserTable(name={self.name}, \r\n email={self.email}, \r\n password={self.password})>"
