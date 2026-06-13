# utils/gpio_sim.py
from robot.libraries.BuiltIn import BuiltIn
import threading
import time

class GPIOPin:
    def __init__(self, pin_number):
        self.pin_number = pin_number
        self._state = 0
        self._lock = threading.Lock()
        self._callback = None
        self._debounce_ms = 0
        self._last_event_ts = 0
        self._edge = 'both'

    def _should_fire(self, new_state):
        now = time.time() * 1000
        if self._debounce_ms and (now - self._last_event_ts) < self._debounce_ms:
            return False
        if self._edge == 'both':
            return True
        if self._edge == 'rising' and new_state == 1 and self._state == 0:
            return True
        if self._edge == 'falling' and new_state == 0 and self._state == 1:
            return True
        return False

    def set_high(self):
        with self._lock:
            new_state = 1
            if self._should_fire(new_state):
                self._state = new_state
                self._last_event_ts = time.time() * 1000
                self._fire_callback(new_state)
            else:
                self._state = new_state

    def set_low(self):
        with self._lock:
            new_state = 0
            if self._should_fire(new_state):
                self._state = new_state
                self._last_event_ts = time.time() * 1000
                self._fire_callback(new_state)
            else:
                self._state = new_state

    def read_state(self):
        with self._lock:
            return self._state

    def register_interrupt(self, callback, debounce_ms=0, edge='both', async_callback=True):
        """Register interrupt with debounce and edge selection."""
        self._callback = callback
        self._debounce_ms = debounce_ms
        self._edge = edge
        self._async = async_callback

    def _fire_callback(self, state):
        if not self._callback:
            return
        if getattr(self, '_async', True):
            threading.Thread(target=self._callback, args=(self.pin_number, state), daemon=True).start()
        else:
            self._callback(self.pin_number, state)


class GPIOSimulation:
    """Robot Framework library for GPIO simulation."""

    def __init__(self):
        self.pins = {}

    def _get_pin(self, pin_number):
        return self.pins.setdefault(pin_number, GPIOPin(pin_number))

    def set_high(self, pin_number):
        self._get_pin(pin_number).set_high()

    def set_low(self, pin_number):
        self._get_pin(pin_number).set_low()

    def read_state(self, pin_number):
        return self._get_pin(pin_number).read_state()

    def register_interrupt(self, pin_number, keyword_name=None, *args, debounce_ms=0, edge='both', async_callback=True):
        def cb(pin, state):
            if keyword_name:
                BuiltIn().run_keyword(keyword_name, *args, pin, state)
        pin = self._get_pin(pin_number)
        pin.register_interrupt(cb, debounce_ms=debounce_ms, edge=edge, async_callback=async_callback)
