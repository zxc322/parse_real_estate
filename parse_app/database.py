from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer, inspect
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy_utils import database_exists, create_database

from settings import postgresql as pg_settings


#  init database

def get_engine(user, pswd, host, port, db):
    url = f'postgresql://{user}:{pswd}@{host}:{port}/{db}'
    if not database_exists:
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=True)
    return engine

def get_engine_from_settings():
    keys = ['pguser', 'pgpswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in pg_settings.keys()):
        raise Exception ('Bad config file')

    return get_engine(pg_settings['pguser'],pg_settings['pgpswd'],pg_settings['pghost'],pg_settings['pgport'],pg_settings['pgdb'])



engine = get_engine_from_settings()

if not inspect(engine).has_table("apartaments"):

    meta = MetaData()

    real_estate = Table('apartaments', meta,
            Column('id', Integer, primary_key=True),
            Column('image', String(2000), nullable=False),
            Column('title', String(2000), nullable=False),
            Column('location', String(100), nullable=False),
            Column('published_date', String(50), nullable=False),
            Column('bedrooms', String(100), nullable=True),
            Column('description', String(2000), nullable=False),
            Column('currency', String(10), nullable=True),
            Column('price', String(100), nullable=False),
    )
    real_estate.create(engine)
else:
    meta = MetaData(engine)
    real_estate = Table('apartaments', meta, autoload=True) 

conn = engine.connect()


def insert_data_into_db(data):
    conn.execute(real_estate.insert().values(
        image=data.get('image'),
        title=data.get('title'),
        location=data.get('location'),
        published_date=data.get('published_date'),
        bedrooms=data.get('bedrooms'),
        description=data.get('description'),
        currency=data.get('full_price')[0],
        price=data.get('full_price')[1]
    ))



