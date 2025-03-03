from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Project(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10, max_length=500)
    created_at: Optional[datetime] = None
    user_id: int

    class Config:
        schema_extra = {
            'example': {
                'name': 'Detección de EPP',
                'description': 'Proyecto de visión por computadora para detección de EPP.',
                'user_id': 1
            }
        }
