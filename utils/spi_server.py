import socket

# Use package-relative import; run with `python -m utils.spi_server` or via the provided launcher
from .sensor_sim import TempSensorSimulation

HOST = "127.0.0.1"
PORT = 65432  # or use a UNIX socket path if preferred

def start_spi_server():
    sensor = TempSensorSimulation(seed=123, noise=0.3)
    sensor.enable_error_mode(False)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"SPI simulation server listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                cmd = data.decode().strip()
                if cmd == "READ_TEMP":
                    value = sensor.read_value()
                    frame = f"TEMP:{value}"
                    conn.sendall(frame.encode())
                elif cmd == "ENABLE_ERROR":
                    sensor.enable_error_mode(True)
                    conn.sendall(b"ERROR_MODE_ON")
                elif cmd == "DISABLE_ERROR":
                    sensor.enable_error_mode(False)
                    conn.sendall(b"ERROR_MODE_OFF")
                else:
                    conn.sendall(b"UNKNOWN_CMD")

if __name__ == "__main__":
    start_spi_server()
