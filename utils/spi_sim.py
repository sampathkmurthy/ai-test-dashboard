from utils.sensor_sim import TempSensorSimulation
from robot.libraries.BuiltIn import BuiltIn

class SPISimulation:
    def __init__(self):
        # By default, attach a TempSensorSimulation
        self.sensor = TempSensorSimulation()
        self.buffer = []

    def attach_sensor(self, sensor=None):
        """Attach a sensor object; if none provided, create a new TempSensorSimulation"""
        if sensor is None:
            self.sensor = TempSensorSimulation()
            return
        if isinstance(sensor, str):
            self.sensor = BuiltIn().get_library_instance(sensor)
        else:
            self.sensor = sensor

    def transfer(self, data):
        """Simulate SPI transfer to read sensor value"""
        if data == "READ_TEMP" and self.sensor:
            value = self.sensor.read_value()
            frame = f"TEMP:{value}"
            self.buffer.append(frame)
            return frame
        return "NO_SENSOR"
