from .driver import Driver
import subprocess

class Ubuntu(Driver):
    def update():
        subprocess.run(["sudo", "apt", "upgrade"])

    def check_updates(self):
        result = subprocess.run(
            ["apt", "list", "--upgradable"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        if result.returncode == 0:
            return str(sum(
                1 for line in result.stdout.splitlines()
                if line and not line.startswith("Listing")
            ))
        raise Error()
