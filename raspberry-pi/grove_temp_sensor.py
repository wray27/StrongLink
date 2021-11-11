'''
Hat Name = 'Grove Base Hat RPi'
<pin> could be one of below values in the pin column for GPIO function
   And connect the device to corresponding slot
==============
 pin | slot
==============
  5  | D5
 12  | PWM
 16  | D16
 18  | D18
 22  | D22
 24  | D24
 26  | D26

'''

import seeed_dht
import logging
import asyncio
import pyodbc
from datetime import datetime
from iot import send_message

def get_temp_humd_reading():
    # for DHT11/DHT22
    sensor = seeed_dht.DHT("11", 5)
    try:
        humi, temp = sensor.read()
        if humi is not None:
            return humi, temp
    except Exception as e:
        print(f"DHT read error: {e}")
        return "-1,-1"

async def insert_temp_into_database():
    now = datetime.utcnow()
    # server = 'tcp:<server_name>.database.windows.net'
    # database = ''
    # username = ''
    # password = ''
    # cnxn = pyodbc.connect(driver ='/usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so',
			# server = server, database = database, uid = username, pwd = password,
			# TDS_Version = '4,2', port = 1433)
    # cursor = cnxn.cursor()
    # insert_temp_reading_to_db = cursor.execute(""INSERT INTO warehouse_data (LocationName, Status, Temperature, Latitude, Longitude, Time)
	# VALUES (?,?,?,?,?,?)"",
	# 'Warehouse-0004', 'ok', temp, 51.5124, -0.0945, now)

    # cnxn.commit()
    humidity, temperature = get_temp_humd_reading()
    logging.basicConfig(filename='/home/pi/Desktop/sensor_readings.log', format='%(asctime)s %(levelname)s:%(name)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)

    logger = logging.getLogger('dht')
    logger_iot = logging.getLogger('azure.iot.device')
    logger_iot.setLevel(logging.WARNING)

    logger.info(f"Temperature reading is {temperature}. Humidity reading is {humidity}")

    message = {
        "temperature": temperature,
        "status": "ok",
        "latitude": 51.5124,
        "longitude": -0.0945,
        "time": now.strftime("%Y-%m-%d %H:%M:%S.%f")
    }

    await send_message(str(message))

    logger.info(f"Inserted temperature reading into the database {message}")



if __name__== "__main__":

    # humidity, temperature = get_temp_humd_reading()
    # logging.basicConfig(filename='/home/pi/Desktop/sensor_readings.log', format='%(asctime)s %(levelname)s:%(name)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)

    # logger = logging.getLogger('dht')
    # logger_iot = logging.getLogger('azure.iot.device')
    # logger_iot.setLevel(logging.WARNING)

    # logger.info(f"Temperature reading is {temperature}. Humidity reading is {humidity}")

    asyncio.run(insert_temp_into_database())

    #logger.info("Inserted temperature reading into the database")
