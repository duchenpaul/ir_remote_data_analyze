import logging
import time

import requests
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import table, column, select


import config

url = config.IR_TRANSPONDER_URL + '/play'

# engine = config.sqlite_engine
engine = config.mysql_engine

metadata = MetaData()
vw_ir_remote_info = Table('vw_ir_remote_info', metadata,
                          autoload=True, autoload_with=engine)


def ir_data_send(device_name, rc_button):
    cmd = '{}.{}'.format(device_name, rc_button)

    print('Sending command ' + cmd)
    rawDataSelect = select([vw_ir_remote_info.c.rawData]).where(
        vw_ir_remote_info.c.device_name == device_name).where(vw_ir_remote_info.c.rc_button == rc_button)

    with engine.connect() as conn:
        result = conn.execute(rawDataSelect)
        rawDataSet = result.fetchone()

    try:
        assert rawDataSet
    except AssertionError as e:
        raise AssertionError('Data not found for ' + cmd)

    rawData = rawDataSet[0]
    data = 'timings=' + ','.join([x.strip() for x in rawData.split(',')])

    header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    try:
        resp = requests.post(url, data=data, headers=header, timeout=10)
        response_text = resp.text
    except requests.exceptions.ConnectTimeout as e:
        logging.error('IR blaster is not reachable')
    except Exception as e:
        raise
    else:
        print('Sent')
        time.sleep(50 / 1000)
    return response_text


if __name__ == '__main__':
    device_name = 'air_conditioner'
    rc_button = 'ONOFF'
    ir_data_send(device_name, rc_button)




