import board
import adafruit_ltr390

class UVSensor:
    def __init__(self):
        self.i2c = board.I2C()
        self.ltr390 = adafruit_ltr390.LTR390(self.i2c)

    def read_data(self):
        return {
            "uv_index": self.ltr390.uvi,
            "lux": self.ltr390.lux,
        }
