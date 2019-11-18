from sqlalchemy import create_engine
import pandas as pd

import toolkit_sqlite

import ir_remote_data_reader

import config

DB_FILE = config.SQLITE_CONFIG['db_file']


def insert_to_db(data_dict, device_name, rc_button):
    data_dict['comment'] = ''
    df = pd.DataFrame([data_dict])

    df_dev = dict()
    df_dev['device_name'] = device_name
    # wind speed: 0: auto, 1: light, 2: mid, 3: max
    df_dev['rc_button'] = rc_button
    df_dev['rc_button_data'] = data_dict['data']
    df_dev = pd.DataFrame([df_dev])

    with toolkit_sqlite.SqliteDB(DB_FILE) as sqlitedb:
        df.to_sql('ir_remote_data', sqlitedb.conn,
                  if_exists='append', index=False)
        df_dev.to_sql('ir_remote_device', sqlitedb.conn,
                      if_exists='append', index=False)

    engine = config.mysql_engine

    with engine.connect() as conn:
        with conn.begin():
            df.to_sql('ir_remote_data', conn,
                      if_exists='append', index=False)
            df_dev.to_sql('ir_remote_device', conn,
                          if_exists='append', index=False)


if __name__ == '__main__':
    data_dict = ir_remote_data_reader.ir_data_read_extract()
    device_name = 'speaker_remote'
    rc_button = 'button_9'
    insert_to_db(data_dict, device_name, rc_button)
