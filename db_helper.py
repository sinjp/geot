from sqlalchemy import create_engine, MetaData


def connect_postgres(user='sand', password='box', db='geot', host='localhost', port=5432):
    """Return connection and metadata objects"""
    con = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}',
                        client_encoding='utf8', echo=True)
    meta = MetaData(bind=con, reflect=True)
    return con, meta
