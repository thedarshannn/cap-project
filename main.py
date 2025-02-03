import time
import RPi.GPIO as GPIO
from uv_sensor import UVSensor
from soil_moisture_sensor import SoilMoistureSensor
from water_level_sensor import WaterLevelSensor

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

uv_sensor = UVSensor()
soil_sensor = SoilMoistureSensor()
water_sensor = WaterLevelSensor()

try:
    while True:
        uv_data = uv_sensor.read_data()
        print(f"UV Index: {uv_data['uv_index']}, Lux: {uv_data['lux']}")

        soil_moisture = soil_sensor.read_moisture()
        if soil_moisture is not None:
            print(f"Soil Moisture Level: {soil_moisture}")

        water_level = water_sensor.calculate_water_level()
        print(f"Water Level: {water_level}%")

        if water_level > 70:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Water level above 70%. LED ON.")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    GPIO.cleanup()
