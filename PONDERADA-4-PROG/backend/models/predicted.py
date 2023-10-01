from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from config.db import base

class PredictTable(base):
    __tablename__ = 'predict'
    predictId = Column(Integer,primary_key=True, autoincrement=True)
    age = Column(Integer, nullable=False)
    hypertension = Column(Integer, nullable=False)
    heart_disease = Column(Integer, nullable=False)
    work_type = Column(Integer, nullable=False)
    avg_glucose_level = Column(Float, nullable=False)
    bmi = Column(Float, nullable=False)
    predicted = Column(Integer, nullable=False)
    userId = mapped_column(Integer, ForeignKey('user.userId'))

    def __init__(self, age, hypertension, heart_disease, work_type, avg_glucose_level, bmi, predicted):
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.work_type = work_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.predict = predicted

    def __repr__(self):
        return f"<PredictTable(age={self.age}, \r\n hypertension={self.hypertension}, \r\n heart_disease={self.heart_disease}, \r\n work_type={self.work_type}, \r\n avg_glucose_level={self.avg_glucose_level}, \r\n bmi={self.bmi}, \r\n predicted={self.predicted})>"