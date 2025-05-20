from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Person(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    birth_date: Optional[date] = None
    phone: Optional[str] = Field(None, max_length=20)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao@example.com",
                "birth_date": "1990-01-01",
                "phone": "(11) 98765-4321"
            }
        } 