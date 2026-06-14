import random
from robot.libraries.BuiltIn import BuiltIn

class TempSensorSimulation:
    def __init__(self, seed = 42, noise=0.5):
        random.seed(seed)
        self.noise = noise
        self.base_tem = 25.0
        self.error_mode = False

    def set_seed(self, seed):
        random.seed(seed)

    def enable_error_mode(self, enabled=True):
        self.error_mode = enabled

    def read_value(self):
        if self.error_mode and random.random() < 0.2:
            return "CRC_ERROR"
        noise = (random.random() - 0.5) * self.noise
        return round(self.base_tem + noise, 2)    