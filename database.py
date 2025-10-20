from sqlalchemy import (
    create_engine ,URL,
    Table, Column, INTEGER, String, BOOLEAN, MetaData
                        
    
                        
) 
from config import HOST, PASSWORD, USER, DATABASE, PORT

url_object = URL.create(
    "postgresql+psycopg2",
    username = USER,
    port = PORT,
    password = PASSWORD,
    database = DATABASE,
    host = HOST
)
engine = create_engine(url_object)

meta = MetaData()

users = Table(
    'user',
    meta,
    Column('first_name ', String(length=64), nullable=False),
    Column('last_name', String(length=65)),
    Column('is_male', BOOLEAN()),
)

meta.create_all(engine)


