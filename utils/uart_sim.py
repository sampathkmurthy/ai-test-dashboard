import random

class UARTSimulation(object):   # Explicitly inherit from object
    """Simulated UART driver for Robot Framework."""

    def __init__(self):
        self.buffer = []
        self.error_mode = False

    def enable_error_mode(self, flag=True):
        """Enable or disable error injection."""
        if isinstance(flag, str):
            flag = flag.lower() in ["true", "1", "yes"]
        self.error_mode = flag
        print(f"Error mode set to {self.error_mode}")

    def send(self, message):
        if self.error_mode and random.choice([True, False]):
            print(f"UART TX ERROR: {message}")
            self.buffer.append("CORRUPTED")
        else:
            print(f"UART TX: {message}")
            self.buffer.append(message)

    def receive(self):
        if self.buffer:
            msg = self.buffer.pop(0)
            print(f"UART RX: {msg}")
            return msg
        return ""
