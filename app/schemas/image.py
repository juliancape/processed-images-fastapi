from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Image(BaseModel):
    id: Optional[int] = None
    filename: str = Field(min_length=3, max_length=255)
    content_type: str = Field(min_length=3, max_length=50)
    data: bytes
    inserted_at: Optional[datetime] = None
    project_id: int

    class Config:
        schema_extra = {
            'example': {
                'filename': 'imagen_original.jpg',
                'content_type': 'image/jpeg',
                'data': 'base64encodeddata==',
                'project_id': 1
            }
        }
