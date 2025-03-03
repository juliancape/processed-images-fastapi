from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from service.image_service import ImageService
from schemas.image import Image
from fastapi.encoders import jsonable_encoder


image_router = APIRouter()

@image_router.get('/images', tags=['images'], response_model=List[Image])
def get_images():
    db = Session()
    result = ImageService(db).get_images()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@image_router.get('/images/{id}', tags=['images'], response_model=Image)
def get_image(id: int = Path(ge=1)):
    db = Session()
    result = ImageService(db).get_image(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Imagen no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@image_router.post('/images', tags=['images'], response_model=dict, status_code=201)
def create_image(image: Image):
    db = Session()
    ImageService(db).create_image(image)
    return JSONResponse(status_code=201, content={"message": "Imagen subida correctamente"})

@image_router.delete('/images/{id}', tags=['images'], response_model=dict)
def delete_image(id: int):
    db = Session()
    if not ImageService(db).get_image(id):
        return JSONResponse(status_code=404, content={'message': 'Imagen no encontrada'})
    
    ImageService(db).delete_image(id)
    return JSONResponse(status_code=200, content={"message": "Imagen eliminada correctamente"})
