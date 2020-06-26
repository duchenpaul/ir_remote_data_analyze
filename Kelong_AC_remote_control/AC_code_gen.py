import itertools
'''
Air conditioner mode format: `<MODE>-<WIND SPEED>-<FLAPS>-<TEMPERATURE>`
- MODE: heat/cool
- WIND SPEED: auto/high/mid/low
- FLAPS: on/off
- TEMPERATURE: 16~31
'''

mode_list = ['cool']
wind_speed_list = ['high', 'mid',]
flaps_list = ['on', 'off']
temperature_list = range(25, 31)

idx = 1
for x in itertools.product(mode_list, wind_speed_list, flaps_list, temperature_list):
    print(idx, x)
    idx += 1
    mode, wind_speed, flaps, temperature = x
    rc_button = '%(mode)s-%(wind_speed)s-%(flaps)s-%(temperature)s' % vars()
    print(rc_button)
