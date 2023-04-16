import os
import pandas
from sqlalchemy import create_engine
from sqlalchemy import text

USERNAME = os.getenv("MASTER_DB_USERNAME")
PASSWORD = os.getenv("MASTER_DB_PASSWORD")
DATABASE_HOST = os.getenv('MASTER_DB_HOSTNAME')
DATABASE_PORT = os.getenv('MASTER_DATABASE_PORT')
DATABASE_NAME = os.getenv('MASTER_DATABASE_NAME')

def create_database():
    connection_string = 'mysql+pymysql://%s:%s@%s:%s' % (USERNAME, PASSWORD, DATABASE_HOST, DATABASE_PORT)
    #print(connection_string)
    engine= create_engine(connection_string)
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE %s" % DATABASE_NAME))
    engine.dispose()

def load_data():
    print("Reading data from excel:")
    df = pandas.read_excel('/python-docker/user_data.xlsx',sheet_name = 'in')
    print("Reading completed. Writing data to DB")
    print("Creating database")
    create_database()
    connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (USERNAME, PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)
    #print(connection_string)
    engine = create_engine(connection_string)
    df.to_sql('user_data', con=engine)
    print("Writing to database completed")
    engine.dispose()

def read_data_from_db():
    connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
    USERNAME, PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)
    print(connection_string)
    engine = create_engine(connection_string,echo=True)
    with engine.connect() as connection:
        data = connection.execute(text("SELECT * FROM user_data")).fetchall()


load_data()