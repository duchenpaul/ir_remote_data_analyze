[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# infrared remote control data analyze tool
use [esp8266_ir_blaster](https://github.com/duchenpaul/esp8266_ir_blaster) to get data from infrared, analyze and load to database

# Air conditioner coding format
Air conditioner mode format: `<MODE>-<WIND SPEED>-<FLAPS>-<TEMPERATURE>`
- MODE: heat/cool
- WIND SPEED: auto/high/mid/low
- FLAPS: on/off
- TEMPERATURE: 16~31

example: `cool-high-on-28`

reference: [NEC IR Remote Control Interface with 8051](https://exploreembedded.com/wiki/NEC_IR_Remote_Control_Interface_with_8051)