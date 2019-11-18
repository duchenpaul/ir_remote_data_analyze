import sqlite3
import pandas as pd
from sqlalchemy import create_engine, MetaData

DB_FILE = r'ir_remote_data.db'
# DB_FILE = r'C:\Users\chdu\Desktop\Portal\Other\tidal_job_extract\tidal_database.db'

SOURCE_TABLE_NAME_LIST = ['ir_remote_data', 'ir_remote_device', ]


def sync_table(SOURCE_TABLE_NAME):
    # tidal_job__prd
    print('Syncing {}'.format(SOURCE_TABLE_NAME))
    TARGET_TABLE_NAME = SOURCE_TABLE_NAME
    # TARGET_TABLE_NAME = 'ctl_rs_process_sql_META'

    engine = create_engine('sqlite:///{}'.format(DB_FILE), echo=False)
    metadata = MetaData(engine)

    with engine.connect() as conn:
        with conn.begin():
            df = pd.read_sql_table(SOURCE_TABLE_NAME, conn)

    # print(df)

    mysql_config = {
        'user': 'pi',
        'password': 'raspberry',
        'server': 'rpi',
        'database': 'test',
    }

    engine = create_engine(
        'mysql://{user}:{password}@{server}/{database}'.format(**mysql_config))

    with engine.connect() as conn:
        with conn.begin():
            df.to_sql(TARGET_TABLE_NAME, con=engine,
                      if_exists='replace', index=False)


if __name__ == '__main__':
    for i in SOURCE_TABLE_NAME_LIST:
        sync_table(i)
