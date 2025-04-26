from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para hashear la contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar la contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    print(pwd_context.verify(plain_password, hashed_password), plain_password,hashed_password )
    return pwd_context.verify(plain_password, hashed_password)

