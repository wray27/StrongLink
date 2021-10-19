import os
import time
import math
import random
import asyncio
import numpy as np
from datetime import datetime, date

from iot import send_message

class Sensor:

    def __init__(self):
        self.coordinates = [
            [51.5074, 0.1278], [51.7520, 1.2577], [52.2053, 0.1218], [53.4808, 2.2426],
            [53.4084, 2.9916], [55.9533, 3.1883], [53.8008, 1.5491], [53.8008, 1.5491],
            [50.8225, 0.1372], [52.4862, 1.8904]
        ]
        self.location_setup(self.coordinates[random.randint(0, 9)])
        self._dropoff_count = 0

    def get_destination_coordinates(self, start):
        destination = self.coordinates[random.randint(0, 9)]
        while self.are_coordinates_equal(start, destination):
            destination = self.coordinates[random.randint(0, 9)]
        return destination

    def location_setup(self, start):
        self._start = start
        print("\n")
        print("Setting Location...")
        print("Start:")
        self.print_coordinate(self._start)
        self._destination = self.get_destination_coordinates(start)
        print("Destination:")
        self.print_coordinate(self._destination)
        print("\n")
        self._current_location = self._start
        difference = np.subtract(self._destination, self._start)
        interval = random.randint(20, 50)
        self._step = difference / interval

    def are_coordinates_equal(self, start, destination):
        rel_tol = 1e-06
        return (math.isclose(start[0], destination[0], rel_tol=rel_tol) and
            math.isclose(start[1], destination[1], rel_tol=rel_tol))

    def record_location(self):
        if not self.are_coordinates_equal(self._current_location, self._destination):
            self._current_location += self._step
        else:
            self.location_setup(self._destination)
            self._dropoff_count += 1
        self.print_coordinate(self._current_location)

    def print_coordinate(self, coordinate):
        print(f"lat: {coordinate[0]}°, long: {coordinate[1]}°")

    def record_temperature(self):
        temp = random.randint(1, 20)
        print(f"temp: {temp}°C")
        return temp

    def set_status(self, temperature):
        status = ""
        if (temperature < 4) or (temperature > 16):
            status = "out_of_range"
        else:
            status = "ok"
        print(f"status: {status}")


    def create_message(self):
        self.record_location()
        temperature = self.record_temperature()
        message = {
            "dropoff_count": self._dropoff_count,
            "temperature": temperature,
            "status": self.set_status(temperature),
            "latitude": self._current_location[0],
            "longitude": self._current_location[1],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }
        return str(message)


async def simulate(interval):
    sensor = Sensor()
    while True:
        message = sensor.create_message()
        # await send_message(message)
        time.sleep(interval)

if __name__ == "__main__":
    asyncio.run(simulate(600))