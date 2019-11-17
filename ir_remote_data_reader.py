import requests
import time

import toolkit_text

url = r'http://192.168.31.173/record'

MAX_TRY = 10


def ir_data_read():
    tried_times = 0
    response_text = 'empty'
    print('Recieving remote data', end='',)
    while response_text == 'empty' and tried_times < MAX_TRY:
        resp = requests.get(url, timeout=10)
        response_text = resp.text
        if response_text == 'FFFFFFFFFFFFFFFF':
            print('Bad data recieved, retry')
            tried_times -= 1
            continue
        tried_times += 1
        time.sleep(1)
        print('.', end='',)
    print('\n', end='',)
    try:
        assert response_text != 'empty'
    except AssertionError as e:
        raise Exception('Did not recieve any data')
    
    return response_text


def extract_value(pattern, ir_data_raw):
    try:
        return toolkit_text.regex_find(pattern, ir_data_raw)[0]
    except IndexError as e:
        return None


def ir_data_extract(ir_data_raw):
    rtn_data = dict()
    rawData_pattern = r'''(?<=\{)(.*)(?=\})'''
    rawData = extract_value(rawData_pattern, ir_data_raw)
    rtn_data['rawData'] = rawData

    addressData_pattern = r'''(?<=uint32_t address \= )(.*)(?=\;)'''
    address = extract_value(addressData_pattern, ir_data_raw)
    rtn_data['address'] = address

    commandData_pattern = r'''(?<=uint32_t command \= )(.*)(?=\;)'''
    command = extract_value(commandData_pattern, ir_data_raw)
    rtn_data['command'] = command

    type_pattern = r'''(?<=// )(.*)(?= )'''
    _type = extract_value(type_pattern, ir_data_raw)
    rtn_data['type'] = _type

    data_pattern = r'''(?<=// )(.*)'''
    data = extract_value(data_pattern, ir_data_raw)
    rtn_data['data'] = data.replace(_type, '').strip()
    return rtn_data


def ir_data_read_extract():
    return ir_data_extract(ir_data_read())


if __name__ == '__main__':
    response_text = ir_data_read()
    print(response_text)

    # response_text = '''uint16_t rawData[99] = {8846, 4464,  542, 1686,  518, 1686,  492, 598,  516, 598,  490, 622,  492, 596,  492, 624,  492, 1712,  492, 596,  492, 1712,  492, 1712,  492, 596,  518, 598,  492, 596,  518, 598,  492, 598,  516, 598,  492, 596,  492, 624,  490, 598,  492, 622,  492, 596,  492, 624,  492, 598,  490, 622,  492, 1686,  518, 596,  492, 598,  518, 1686,  518, 596,  492, 598,  518, 1686,  492, 622,  492, 596,  492, 622,  492, 598,  492, 622,  492, 596,  492, 622,  492, 596,  492, 624,  496, 592,  492, 596,  518, 596,  492, 598,  518, 596,  492, 570,  544, 598,  492};  // UNKNOWN 90DE683D'''
    rtn_data = ir_data_extract(response_text)
    print(rtn_data)
    print(len([x.split() for x in rtn_data['rawData'].split(',')]))
