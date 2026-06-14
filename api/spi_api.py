import subprocess

import subprocess

def run_firmware(command):
    """Run firmware.exe with a simulated SPI command via cmd.exe and capture output."""
    result = subprocess.run(
        ["cmd.exe", "/c", "firmware.exe", command],
        capture_output=True,
        text=True,
        shell=False
    )
    return result.stdout.strip()

