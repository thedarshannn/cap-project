import smbus

class WaterLevelSensor:
    def __init__(self, bus_number=1, low_addr=0x77, high_addr=0x78, threshold=100):
        self.bus = smbus.SMBus(bus_number)
        self.low_addr = low_addr
        self.high_addr = high_addr
        self.threshold = threshold

    def get_low_sections(self):
        try:
            return self.bus.read_i2c_block_data(self.low_addr, 0, 8)
        except Exception as e:
            print(f"Error reading low water level sections: {e}")
            return []

    def get_high_sections(self):
        try:
            return self.bus.read_i2c_block_data(self.high_addr, 0, 12)
        except Exception as e:
            print(f"Error reading high water level sections: {e}")
            return []

    def calculate_water_level(self):
        low_data = self.get_low_sections()
        high_data = self.get_high_sections()

        touch_val = 0
        for i in range(8):
            if low_data and low_data[i] > self.threshold:
                touch_val |= 1 << i
        for i in range(12):
            if high_data and high_data[i] > self.threshold:
                touch_val |= 1 << (8 + i)

        trig_section = 0
        while touch_val & 0x01:
            trig_section += 1
            touch_val >>= 1

        return trig_section * 5