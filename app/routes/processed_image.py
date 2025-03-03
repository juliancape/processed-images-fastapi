from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from service.processed_image_service import ProcessedImageService
from schemas.processed_image import ProcessedImage
from fastapi.encoders import jsonable_encoder

processed_image_router = APIRouter()

@processed_image_router.get('/processed_images', tags=['processed_images'], response_model=List[ProcessedImage])
def get_processed_images():
    db = Session()
    result = ProcessedImageService(db).get_processed_images()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@processed_image_router.get('/processed_images/{id}', tags=['processed_images'], response_model=ProcessedImage)
def get_processed_image(id: int = Path(ge=1)):
    db = Session()
    result = ProcessedImageService(db).get_processed_image(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Imagen procesada no encontrada'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@processed_image_router.post('/processed_images', tags=['processed_images'], response_model=dict, status_code=201)
def create_processed_image(processed_image: ProcessedImage):
    db = Session()
    ProcessedImageService(db).create_processed_image(processed_image)
    return JSONResponse(status_code=201, content={"message": "Imagen procesada guardada correctamente"})

@processed_image_router.delete('/processed_images/{id}', tags=['processed_images'], response_model=dict)
def delete_processed_image(id: int):
    db = Session()
    if not ProcessedImageService(db).get_processed_image(id):
        return JSONResponse(status_code=404, content={'message': 'Imagen procesada no encontrada'})
    
    ProcessedImageService(db).delete_processed_image(id)
    return JSONResponse(status_code=200, content={"message": "Imagen procesada eliminada correctamente"})
