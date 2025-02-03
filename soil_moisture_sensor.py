import smbus

class SoilMoistureSensor:
    def __init__(self, bus_number=1, address=0x28):
        self.bus = smbus.SMBus(bus_number)
        self.address = address

    def read_moisture(self):
        try:
            data = self.bus.read_i2c_block_data(self.address, 0x05, 2)
            moisture_level = data[1] << 8 | data[0]
            return moisture_level
        except Exception as e:
            print(f"Error reading soil moisture: {e}")
            return None