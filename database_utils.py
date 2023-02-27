from sqlalchemy import create_engine, inspect
import yaml

class DatabaseConnector:
    def __init__(self):
        self.rds_dict = self.read_db_creds()

    def read_db_creds(self):
        with open('db_creds.yaml', 'r') as creds:
            rds_dict=yaml.safe_load(creds)
        return rds_dict
    
    def init_db_engine(self):     #engine creation for sqlalchemy
        # print(self.read_db_creds)
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{self.rds_dict['RDS_USER']}:{self.rds_dict['RDS_PASSWORD']}@{self.rds_dict['RDS_HOST']}:{self.rds_dict['RDS_PORT']}/{self.rds_dict['RDS_DATABASE']}")
        return engine
