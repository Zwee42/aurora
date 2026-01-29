from .driver import Driver
import subprocess

class Archlinux(Driver):
    def update():
        pass

    def check_updates(self):
        result = subprocess.run(["checkupdates"], capture_output=True, text=True)
        if result.returncode == 0:
            return str(len(result.stdout.splitlines()))
        raise Error()
