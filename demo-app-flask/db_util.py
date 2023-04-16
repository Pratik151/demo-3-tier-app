import os
from sqlalchemy import create_engine
from sqlalchemy import text


MASTER_DB_USERNAME=os.getenv("MASTER_DB_USERNAME")
MASTER_DB_PASSWORD=os.getenv("MASTER_DB_PASSWORD")
MASTER_DB_HOSTNAME=os.getenv('MASTER_DB_HOSTNAME')
MASTER_DATABASE_PORT=os.getenv('MASTER_DATABASE_PORT')
MASTER_DATABASE_NAME=os.getenv('MASTER_DATABASE_NAME')

READ_DB_USERNAME=os.getenv("READ_DB_USERNAME")
READ_DB_PASSWORD=os.getenv("READ_DB_PASSWORD")
READ_DB_HOSTNAME=os.getenv('READ_DB_HOSTNAME')
READ_DATABASE_PORT=os.getenv('READ_DATABASE_PORT')
READ_DATABASE_NAME=os.getenv('READ_DATABASE_NAME')


MASTER_DB_CONNECTION_STRING = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
    MASTER_DB_USERNAME, MASTER_DB_PASSWORD, MASTER_DB_HOSTNAME, MASTER_DATABASE_PORT, MASTER_DATABASE_NAME)
READ_DB_CONNECTION_STRING = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
    READ_DB_USERNAME, READ_DB_PASSWORD, READ_DB_HOSTNAME, READ_DATABASE_PORT, READ_DATABASE_NAME)

def read_data_from_db(query, operationType='READ'):
    #print(connection_string)
    engine = create_engine(READ_DB_CONNECTION_STRING,echo=True)
    data = None
    with engine.connect() as connection:
        data = connection.execute((text(query))).fetchall()
    return data
