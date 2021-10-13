import os
import time
import asyncio
import random
from datetime import datetime, date

from iot import send_message

def record_temperature():
    temp = random.randint(-10,30)
    print(f"temp: {temp}°C")
    return temp

def create_message():
    message = {
        "temperature": record_temperature(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return str(message)

async def simulate(interval):
    while True:
        message = create_message()
        await send_message(message)
        time.sleep(interval)

if __name__ == "__main__":
    asyncio.run(simulate(10))