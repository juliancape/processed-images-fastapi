from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProcessedImage(BaseModel):
    id: Optional[int] = None
    filename: str = Field(min_length=3, max_length=255)
    content_type: str = Field(min_length=3, max_length=50)
    data: bytes
    inserted_at: Optional[datetime] = None
    image_id: int

    class Config:
        schema_extra = {
            'example': {
                'filename': 'imagen_procesada.jpg',
                'content_type': 'image/jpeg',
                'data': 'base64encodedprocesseddata==',
                'image_id': 1
            }
        }
