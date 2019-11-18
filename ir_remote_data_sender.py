import time

import requests
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import table, column, select

import toolkit_text

import config

url = config.IR_TRANSPONDER_URL + '/play'


DB_FILE = config.SQLITE_CONFIG['db_file']
mysql_config = config.MYSQL_CONFIG


sqlite_engine = create_engine('sqlite:///{}'.format(DB_FILE), echo=False)

mysql_engine = create_engine(
    'mysql://{user}:{password}@{server}/{database}'.format(**mysql_config))

engine = sqlite_engine

metadata = MetaData()
vw_ir_remote_info = Table('vw_ir_remote_info', metadata,
                          autoload=True, autoload_with=engine)


def ir_data_send(device_name, rc_button):
    rawDataSelect = select([vw_ir_remote_info.c.rawData]).where(
        vw_ir_remote_info.c.device_name == device_name).where(vw_ir_remote_info.c.rc_button == rc_button)

    with engine.connect() as conn:
        result = conn.execute(rawDataSelect)
        rawDataSet = result.fetchone()

    try:
        assert rawDataSet
    except AssertionError as e:
        raise Exception('Data not found for {}.{}'.format(
            device_name, rc_button))

    rawData = rawDataSet[0]
    data = 'timings=' + ','.join([x.strip() for x in rawData.split(',')])

    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    try:
        resp = requests.post(url, data=data, headers=header, timeout=10)
        response_text = resp.text
    except Exception as e:
        raise
    return response_text


if __name__ == '__main__':
    device_name = 'speaker_remote'
    rc_button = 'onoff'
    ir_data_send(device_name, rc_button)
