import threading

class GPIOPin:
    #initialize a GPIO pin with a pin number, initial state, and optional callback function
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self.state = 0  # 0 = LOW, 1 = HIGH
        self.callback = None
    
    #set the state of the pin to HIGH and trigger the callback if registered
    def set_high(self):
        self.state = 1
        print(f"Pin {self.pin_number} set HIGH")
        if self.callback:
            threading.Thread(target=self.callback, args=(self.pin_number,)).start()
    
    #set the state of the pin to Low and trigger the caallback if registered
    def set_low(self):
        self.state = 0
        print(f"Pin {self.pin_number} set LOW")
        if self.callback:
            threading.Thread(target=self.callback, args=(self.pin_number,)).start() 

    #read the current state of the pin
    def read_state(self):
        return self.state
    
    #register a callback function to be called when the pin state changes
    def register_interrupt(self, callback):
        self.callback = callback

class GPIOSimulation:
    """Simulated GPIO driver for Robot Framework."""

    #initialize the GPIO simulation with an empty dictionary of pins
    def __init__(self):
        self.pins = {}

    #set the state of a pin to HIGH
    def set_high(self, pin_number):
        pin = self.pins.setdefault(pin_number, GPIOPin(pin_number))
        pin.set_high()

    #set the state of a pin to LOW
    def set_low(self, pin_number):
        pin = self.pins.setdefault(pin_number, GPIOPin(pin_number))
        pin.set_low()

    #read the state of a pin    
    def read_state(self, pin_number):
        pin = self.pins.setdefault(pin_number, GPIOPin(pin_number))
        return pin.read_state()
    
    #register a callback function for a pin interrupt
    def register_interrupt(self, pin_number, callback):
        pin = self.pins.setdefault(pin_number, GPIOPin(pin_number))
        pin.register_interrupt(callback)
