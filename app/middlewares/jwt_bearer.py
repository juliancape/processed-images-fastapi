from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        try:
            # Intentamos validar el token
            data = validate_token(auth.credentials)

            # Si no se encuentra 'email' en los datos decodificados, es inválido
            if not data.get('email'):
                raise HTTPException(status_code=403, detail='Credenciales inválidas')

        except Exception as e:
            # Si el token es inválido o ha expirado
            raise HTTPException(status_code=403, detail=f'Token inválido o expirado: {str(e)}')
