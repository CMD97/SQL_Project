import psycopg2
from sqlalchemy import create_engine
import yaml

class DatabaseConnector:

    def __init__(self):
        pass

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as creds:
            rds_dict=yaml.safe_load(creds)
        print(type(rds_dict))
        return rds_dict
    
   # read_db_creds()
    def init_db_engine(self, rds_dict):
        # rds_dict = db.read_db_creds()
        # engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{rds_dict['RDS_USER']}:{rds_dict['RDS_PASSWORD']}@{rds_dict['RDS_HOST']}:{rds_dict['RDS_PORT']}/{rds_dict['RDS_DATABASE']}")
        # print(engine.connect())
        return engine.connect()

db = DatabaseConnector()
# db.init_db_engine(rds_dict=)
rds_dict = db.read_db_creds()
engine = db.init_db_engine(rds_dict)

        # DATABASE_TYPE = 'postgresql'
        # DBAPI = 'psycopg2'
        # ENDPOINT = 'data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com'
        # USER = 'aicore_admin'
        # PASSWORD = 'AiCore2022'
        # PORT = 5432
        # DATABASE = 'postgres'
        
