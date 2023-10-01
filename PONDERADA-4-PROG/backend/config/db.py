from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('RDS_USERNAME')
password = os.getenv('RDS_PASSWORD')
host = os.getenv('RDS_HOST')
port = os.getenv('RDS_PORT')
db_name = os.getenv('RDS_DB_NAME')


# SQLAlchemy settings
url=f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'
engine=create_engine(url)
base=declarative_base()
metadata=MetaData()
conn=engine.connect()