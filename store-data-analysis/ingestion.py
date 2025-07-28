import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = 'big_project_folder/logs/big_project.log',
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

engine = create_engine("mysql+mysqlconnector://root:Mysqlpswd%40123@localhost:3306/waleeddb")

def load_data():
    '''Loads the csv file in database and logs it '''
    start = time.time()
    for file in os.listdir('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads'):
        if '.csv' in file :
            df = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'+file)
            logging.info(f"ingesting {file} in database")
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = end-start
    logging.info(f'Ingestion complete in {total_time} seconds')

def ingest_db(df, table_name, engine):
    '''reads file and then ingests in the database which is defined in the engine.'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

if __name__ == "__main__":
    load_data()