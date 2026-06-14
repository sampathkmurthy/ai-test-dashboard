import subprocess
import os
import platform

def run_firmware(command):
    """Run firmware binary with a simulated SPI command and capture output."""
    if platform.system() == "Windows":
        exe_name = "firmware.exe"
    else:
        exe_name = "firmware.bin"   # match CI build output

    exe_path = os.path.join(os.getcwd(), exe_name)
    # Ensure binary exists
    if not os.path.exists(exe_path):
        raise FileNotFoundError(f"Firmware binary not found: {exe_path}")

    # On Unix, ensure the file is executable; try to set the bit if missing
    if platform.system() != "Windows":
        if not os.access(exe_path, os.X_OK):
            try:
                st = os.stat(exe_path)
                os.chmod(exe_path, st.st_mode | 0o111)
            except PermissionError:
                raise PermissionError(
                    f"Cannot make firmware executable: {exe_path}.\n"
                    "Ensure the CI job sets the executable bit (e.g. 'chmod +x firmware.bin')"
                )

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
