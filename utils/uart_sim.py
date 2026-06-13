import time
import random
import threading
from collections import deque # Import deque for efficient buffer management

class UARTSimulation(object):   # Explicitly inherit from object
    """Simulated UART driver for Robot Framework."""

    """Initialize the UART simulation with an empty buffer, 
        a lock for thread safety, and a random generator instance."""
    def __init__(self):
        self._buffer = deque()  # Use deque for efficient appends and pops
        self._lock = threading.Lock()  # Lock for thread-safe buffer access
        self._rng = random.Random()  # Create a separate random generator instance
        self.error_mode = False  # Flag to enable/disable error injection
        self.error_prob = 0.5 # Probability of error injection (0 to 1)
        self.delay_ms = 0  # Delay in milliseconds for simulated UART communication

    def set_delay(self, ms):
        """Set artificial delay response time in milliseconds."""
        self.delay_ms = int(ms)

    def set_seed(self, seed):
        """Set the seed for the random generator to ensure reproducibility."""
        self._rng = random.Random(seed)  # Create a new random generator with the specified seed

    def enable_error_mode(self, flag=True, prob=0.5):
        """Enable or disable error injection with probability."""
        if isinstance(flag, str):
            flag = flag.lower() in ["true", "1", "yes"]
        self.error_mode = bool(flag)
        self.error_prob = float(prob)

    def send(self, message):
        """Send a message asynchronously with delay and error injection."""
        def process():
            if self.delay_ms:
                time.sleep(self.delay_ms / 1000.0)
            with self._lock:
                if self.error_mode and self._rng.random() < self.error_prob:
                    self._buffer.append("CORRUPTED")
                else:
                    self._buffer.append(message)
        threading.Thread(target=process, daemon=True).start()

    def receive(self, timeout_ms=0):
        """Receive a message with optional timeout."""
        deadline = time.time() + (timeout_ms / 1000.0) if timeout_ms else None
        while True:
            with self._lock:
                if self._buffer:
                    return self._buffer.popleft()
            if deadline and time.time() > deadline:
                return ""
            if not deadline:
                return ""
            time.sleep(0.001)
