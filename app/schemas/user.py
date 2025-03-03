from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    hashed_password: str = Field(min_length=5)
    inserted_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'John Doe',
                'email': 'johndoe@example.com',
                'hashed_password': 'hashedpassword123'
            }
        }
