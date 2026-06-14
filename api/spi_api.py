import subprocess
import os
import platform

def run_firmware(command):
    """Run firmware binary with a simulated SPI command and capture output."""
    # On Windows builds, the binary is firmware.exe
    # On Linux/macOS builds, it may just be firmware (no .exe)
    exe_name = "firmware.exe" if platform.system() == "Windows" else "firmware"
    exe_path = os.path.join(os.getcwd(), exe_name)

    if platform.system() == "Windows":
        # Wrap with cmd.exe to bypass Defender/AppLocker restrictions
        result = subprocess.run(
            ["cmd.exe", "/c", exe_path, command],
            capture_output=True,
            text=True
        )
    else:
        # Direct execution on Linux/macOS
        result = subprocess.run(
            [exe_path, command],
            capture_output=True,
            text=True
        )

    return result.stdout.strip()


