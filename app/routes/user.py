from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from service.user_service import UserService
from schemas.user import User
from fastapi.encoders import jsonable_encoder

from utils.jwt_manager import create_token
from middlewares.jwt_bearer import JWTBearer
from utils.password_manager import hash_password
from utils.password_manager import verify_password
import logging
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

@user_router.post('/users', tags=['users'], response_model=dict, status_code=201) # , dependencies=[Depends(JWTBearer())]
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
    db = Session()
    user_db = UserService(db).get_user_by_email(user.email)

    if not user_db:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontrado"})
    
    print(f"Usuario encontrado: {user_db.email}, Contraseña ingresada: {user.hashed_password}, Contraseña guardada: {user_db.hashed_password}")

    # Verificar que la contraseña ingresada coincida con el hash en la base de datos
    if not verify_password(user.hashed_password, user_db.hashed_password):
        return JSONResponse(status_code=401, content={"message": "Contraseña incorrecta"})

    # Crear un token de acceso con los datos del usuario (en este caso solo email)
    token: str = create_token({'email': user.email})
    return JSONResponse(status_code=200, content={"token": token})



@user_router.post('/signup', tags=['auth'])
def signup(user: User):
    db = Session()
    if UserService(db).get_user_by_email(user.email):
        return JSONResponse(status_code=400, content={"message": "Usuario ya registrado"})
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Usuario creado exitosamente"})