import pandas as pd

import toolkit_sqlite

import ir_remote_data_reader

DB_FILE = 'test.db'


def insert_to_db(data_dict):
    data_dict['comment'] = ''
    df = pd.DataFrame([data_dict])

    df_dev = dict()
    df_dev['device_name'] = 'air_conditioner'
    df_dev['rc_button'] = 'switch'
    df_dev['rc_button_data'] = data_dict['data']
    df_dev = pd.DataFrame([df_dev])
    
    with toolkit_sqlite.SqliteDB(DB_FILE) as sqlitedb:
        df.to_sql('ir_remote_data', sqlitedb.conn, if_exists='append', index = False)
        df_dev.to_sql('ir_remote_device', sqlitedb.conn, if_exists='append', index = False)


if __name__ == '__main__':
    data_dict = ir_remote_data_reader.ir_data_read_extract()
    insert_to_db(data_dict)