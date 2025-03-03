from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from service.user_service import UserService
from schemas.user import User
from fastapi.encoders import jsonable_encoder

from utils.jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer

user_router = APIRouter()

@user_router.get('/users', tags=['users'], response_model=List[User])
def get_users():
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/{id}', tags=['users'], response_model=User)
def get_user(id: int = Path(ge=1)):
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Usuario no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.post('/users', tags=['users'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_user(user: User):
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Usuario registrado correctamente"})

@user_router.put('/users/{id}', tags=['users'], response_model=dict)
def update_user(id: int, user: User):
    db = Session()
    if not UserService(db).get_user(id):
        return JSONResponse(status_code=404, content={'message': 'Usuario no encontrado'})
    
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message": "Usuario actualizado correctamente"})

@user_router.delete('/users/{id}', tags=['users'], response_model=dict)
def delete_user(id: int):
    db = Session()
    if not UserService(db).get_user(id):
        return JSONResponse(status_code=404, content={'message': 'Usuario no encontrado'})
    
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "Usuario eliminado correctamente"})

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.hashed_password == "admin":
        token: str = create_token({'email': user.email, 'password': user.hashed_password})
        return JSONResponse(status_code=200, content=token)