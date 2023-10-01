from pydantic import BaseModel, Field


class PredictModel(BaseModel):
    age: int = Field(..., title="Age")
    hypertension: int = Field(..., title="Hypertension")
    heart_disease: int = Field(..., title="Heart Disease")
    work_type: int = Field(..., title="Work Type")
    avg_glucose_level: float = Field(..., title="Average Glucose Level")
    bmi: float = Field(..., title="BMI")
    userId: int = Field(..., title="User ID")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 30,
                "hypertension": 0,
                "heart_disease": 0,
                "work_type": 1,
                "avg_glucose_level": 90.5,
                "bmi": 25.0,
                "predicted": 0
            }
        }