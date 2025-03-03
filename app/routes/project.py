from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from service.project_service import ProjectService
from schemas.project import Project
from fastapi.encoders import jsonable_encoder

project_router = APIRouter()

@project_router.get('/projects', tags=['projects'], response_model=List[Project])
def get_projects():
    db = Session()
    result = ProjectService(db).get_projects()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@project_router.get('/projects/{id}', tags=['projects'], response_model=Project)
def get_project(id: int = Path(ge=1)):
    db = Session()
    result = ProjectService(db).get_project(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Proyecto no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@project_router.post('/projects', tags=['projects'], response_model=dict, status_code=201)
def create_project(project: Project):
    db = Session()
    ProjectService(db).create_project(project, project.user_id)
    return JSONResponse(status_code=201, content={"message": "Proyecto creado exitosamente"})

@project_router.put('/projects/{id}', tags=['projects'], response_model=dict)
def update_project(id: int, project: Project):
    db = Session()
    if not ProjectService(db).get_project(id):
        return JSONResponse(status_code=404, content={'message': 'Proyecto no encontrado'})
    
    ProjectService(db).update_project(id, project)
    return JSONResponse(status_code=200, content={"message": "Proyecto actualizado correctamente"})

@project_router.delete('/projects/{id}', tags=['projects'], response_model=dict)
def delete_project(id: int):
    db = Session()
    if not ProjectService(db).get_project(id):
        return JSONResponse(status_code=404, content={'message': 'Proyecto no encontrado'})
    
    ProjectService(db).delete_project(id)
    return JSONResponse(status_code=200, content={"message": "Proyecto eliminado correctamente"})
