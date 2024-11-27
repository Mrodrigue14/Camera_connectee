import os

class ConnectBluetooth:
    def __init__(self, address, volume_level):
        self.address = address
        self.volume_level = volume_level

    def connect_device(self):
        print(f"Connexion au périphérique Bluetooth : {self.address}")
        os.system(f"bluetoothctl connect {self.address} > /dev/null 2>&1")

    def set_volume(self):
        os.system(f"amixer sset 'Master' {self.volume_level}% > /dev/null 2>&1")

