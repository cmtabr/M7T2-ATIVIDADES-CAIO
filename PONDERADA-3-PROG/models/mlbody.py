from pydantic import BaseModel, Field

class MlBody(BaseModel): 
    age: int = Field(...), 
    hypertension: int = Field(...),
    heart_disease: int = Field(...),
    work_type: int = Field(...),
    avg_glucose_level: float = Field(...),
    bmi: float = Field(...)
    class Config():
        schema_extra = {
            "example": {
                "age": 67,
                "hypertension": 0,
                "heart_disease": 1,
                "work_type": 1,
                "avg_glucose_level": 228.69,
                "bmi": 36.6
            }
        }