import sqlite3
import pandas as pd
from sqlalchemy import MetaData

import config


SOURCE_TABLE_NAME_LIST = ['ir_remote_data', 'ir_remote_device', ]


def sync_table(SOURCE_TABLE_NAME):
    # tidal_job__prd
    print('Syncing {}'.format(SOURCE_TABLE_NAME))
    TARGET_TABLE_NAME = SOURCE_TABLE_NAME
    # TARGET_TABLE_NAME = 'ctl_rs_process_sql_META'


    with config.sqlite_engine.connect() as conn:
        with conn.begin():
            df = pd.read_sql_table(SOURCE_TABLE_NAME, conn)


    engine = config.mysql_engine

    with engine.connect() as conn:
        with conn.begin():
            df.to_sql(TARGET_TABLE_NAME, con=engine,
                      if_exists='replace', index=False)


if __name__ == '__main__':
    for i in SOURCE_TABLE_NAME_LIST:
        sync_table(i)
