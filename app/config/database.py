# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql+psycopg://myuser:mypassword@localhost:5432/mydatabase"

# engine = create_engine(DATABASE_URL, echo=True)
# Session = sessionmaker(bind=engine)
# Base = declarative_base()



import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = '../database.sqlite'
#Leer el directorio actual de este archivo
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

#Motor de la base de datos
engine = create_engine(database_url, echo=True)

#Crear una sesion para conectarme a la base de datos
Session = sessionmaker(bind=engine)

#Manejo de las tablas
Base = declarative_base()